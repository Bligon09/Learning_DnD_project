
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from dndmodel import connect_to_db, db
import dndcrud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def homepage():
   
    return render_template('homepage.html')


@app.route('/menu')
def menu():


    return render_template('menu.html')

@app.route('/user', methods =['POST'] )
def register_user():
    user_name = request.form.get('user_name')
    email = request.form.get('email')
    password = request.form.get('password')
    check_email = dndcrud.get_user_by_email(email)

    
    if check_email is not None:
        flash("You can't use that email")

    else:
        new_user = dndcrud.create_user(email, user_name, password)
        db.session.add(new_user)
        db.session.commit()
        flash("Your account has been created")


    return redirect('/menu')

@app.route('/verify-email.json/<email>')
def verify_email(email):

    check_email = dndcrud.get_user_by_email(email)

    
    if check_email is not None:
        return {'checked email': 'Email is not available for use'}
    else:
        return {'checked email': 'Email is available for use'}


@app.route('/login', methods =['POST'] )
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user=dndcrud.get_user_by_email(email)

    if password==user.password:
        session['current_user']=user.user_id
        print(session)
        flash(f'Logged in as {user.user_name}')
        return redirect ('/menu')
    else:
        flash('Wrong password, try again')
        return redirect ('/menu')
    
@app.route('/logout', methods =['POST'] )
def logout():
    del session['current_user']
    return redirect ('/menu')

@app.route('/new-to-roleplaying')
def newroleplayer():


    return render_template('new-to-roleplaying.html')

@app.route('/new-to-dnd')
def new_to_dnd():
   
    return render_template('new-to-dnd.html')

@app.route('/history')
def history():


    return render_template('history.html')

@app.route('/cnamefield')
def cnamefield():
   

    return render_template('cnamefield.html')

@app.route('/cnamefield-info', methods =['POST'] )
def add_namefield():
    user=dndcrud.get_user_info(session['current_user'])
    char_name = request.form.get('cname')
    alignment = request.form.get('alignment')
    background = request.form.get('backgrounds')

    check_user=dndcrud.get_cnamefield_info(user.user_id)
    
    if check_user is not None:
        update_user=dndcrud.updating_cname(char_name, alignment, background, user.user_id)
        db.session.commit()
    else:
        namefield = dndcrud.create_cnamefield_info(char_name, alignment, background, user.user_id)
        db.session.add(namefield)
        db.session.commit()
  
    return redirect ('/cnamefield')



@app.route('/asnskills')
def asnskills():

    ability_scores=["str", "dex", "con", "int", "wis", "cha"]

    namefield=dndcrud.get_cnamefield_info(session['current_user'])
    background=namefield.background

    return render_template('asnskills.html', 
                           ability_scores=ability_scores,
                            background=background)


@app.route('/get-bskills.json')
def get_bskills():
    namefield=dndcrud.get_cnamefield_info(session['current_user'])

    background= namefield.background
    if background=="Folk-hero":
        return {'bskill1': 'Animal Handling', 'bskill2': 'Survival'}
    if background=="Noble":
        return {'bskill1': 'History', 'bskill2': 'Persuasion'}
    if background=="Outlander":
        return {'bskill1': 'Athletics', 'bskill2': 'Survival'}
    if background=="Sailor":
        return {'bskill1': 'Athletics', 'bskill2': 'Perception'}
    if background=="Solider":
        return {'bskill1': 'Athletics', 'bskill2': 'Intimidation'}
    


@app.route('/ability-info', methods=['POST'])
def ability_info():

    user=dndcrud.get_user_info(session['current_user'])

    score_dict={}
    score_dict['str']=int(request.form.get("str"))
    score_dict['dex']=int(request.form.get("dex"))
    score_dict['con']=int(request.form.get("con"))
    score_dict['int']=int(request.form.get("int"))
    score_dict['wis']=int(request.form.get("wis"))
    score_dict['cha']=int(request.form.get("cha"))


    abonus1=request.form.get('abonus1')
    for ascore in score_dict:
        if ascore==abonus1:
            score_dict[ascore]+=1

    abonus2=request.form.get('abonus2')
    for ascore2 in score_dict:
        if ascore2==abonus2:
            score_dict[ascore2]+=1


    check_abil=dndcrud.get_abilities_info(session['current_user'])

    if check_abil is not None:
        ability_info=dndcrud.updating_abilities(str=score_dict['str'],
                                 dex=score_dict['dex'],
                                 con=score_dict['con'],
                                 int=score_dict['int'],
                                 wis=score_dict['wis'],
                                 cha=score_dict['cha'],
                                 user_id=user.user_id)
        db.session.add(ability_info)
        db.session.commit()
    else:
        ability_info=dndcrud.create_abilities(str=score_dict['str'],
                                    dex=score_dict['dex'],
                                    con=score_dict['con'],
                                    int=score_dict['int'],
                                    wis=score_dict['wis'],
                                    cha=score_dict['cha'],
                                    user_id=user.user_id)
        
        db.session.add(ability_info)
        db.session.commit()
    

   

    return redirect('/asnskills')

@app.route('/skills-info', methods=['POST'])
def skills_info():
    user=dndcrud.get_user_info(session['current_user'])

    rskill=request.form.get("rskill")
    cskill1=request.form.get("cskill1")
    cskill2=request.form.get("cskill2")
    namefield=dndcrud.get_cnamefield_info(user.user_id)

    background=namefield.background

    bskill1=""
    bskill2=""

    if background == "Folk-hero":
        bskill1="Animal handling" 
        bskill2= "Survival"
    if background == "Noble":
        bskill1="History" 
        bskill2= "Persuasion"
    if background == "Outlander":
        bskill1="Athletics" 
        bskill2= "Survival"
    if background == "Sailor":
        bskill1="Athletics"
        bskill2= "Perception"
    if background == "Solider":
        bskill1="Athletics"
        bskill2= "Intimidation"

    check_skills=dndcrud.get_skills_info(session['current_user'])

    if check_skills is not None:
        the_skills=dndcrud.update_skills(rskill=rskill,
                                     cskill1=cskill1,
                                     cskill2=cskill2,
                                     bskill1=bskill1,
                                     bskill2=bskill2,
                                     user_id=user.user_id)
        db.session.add(the_skills)
        db.session.commit()
    else:
        the_skills=dndcrud.create_skills(rskill=rskill,
                                        cskill1=cskill1,
                                        cskill2=cskill2,
                                        bskill1=bskill1,
                                        bskill2=bskill2,
                                        user_id=user.user_id)
        db.session.add(the_skills)
        db.session.commit()

    return redirect('/asnskills')


@app.route('/feats')
def feats_page():


    return render_template('feats.html')

@app.route('/create-feats', methods=['POST'])
def add_feats():
    user=dndcrud.get_user_info(session['current_user'])

    feat=request.form.get('feats')
    fighting_style=request.form.get('fighting style')
    
    check_feats=dndcrud.get_feats_info(session['current_user'])

    if check_feats is not None:
        feats=dndcrud.update_feats(feat=feat, 
                               fighting_style=fighting_style, 
                               user_id=user.user_id)
    
        db.session.add(feats)
        db.session.commit()

    else:
        feats=dndcrud.create_feats(feat=feat, 
                                fighting_style=fighting_style, 
                                user_id=user.user_id)
        
        db.session.add(feats)
        db.session.commit()


    return redirect('/feats')



@app.route('/equipment')
def equipment_page():

    return render_template('equipment.html')

@app.route('/add-equipment', methods=['POST'])
def add_equipment():
    """
    This is probably the most complicated part so far. 
    A lot of this will be decided on the backend, running through the
    options in the book, but narrowed down and selected 
    based on the higher of str or dex, and special cavaets if they get
    the styles 'great weapon,' 'two weapon,' and 'archery'
    """

    user=dndcrud.get_user_info(session['current_user'])

    feats=dndcrud.get_feats_info(user.user_id)
    abilities=dndcrud.get_abilities_info(user.user_id)
    equipment_dict={}
    equipment_dict['option4']="explorer's pack"
    armor_class = 0

    if abilities.dex > abilities.str:
        equipment_dict['option1']="leather armor, longbow, 20 arrows"
        equipment_dict['option2']="rapier and dagger"
        equipment_dict['option3']="2 hand axes"
        armor_class= 11 + abilities.dex
        
    else:
        equipment_dict['option1']="chainmail"
        equipment_dict['option2']="longsword and shield"
        equipment_dict['option3']="2 hand axes"
        armor_class=16

    if feats.fighting_style == "Great Weapon Fighting":
        equipment_dict['option2']="Great axe and shield"
    
    if feats.fighting_style == "Two-weapon fighting":
        equipment_dict['option2']="two short swords"
        equipment_dict['option3']="light crossbow and 20 bolts"

    check_equipment=dndcrud.get_equipment_info(user.user_id)

    if check_equipment is not None:

        equipment=dndcrud.update_equipment(option1=equipment_dict['option1'],
                                            option2=equipment_dict['option2'],
                                            option3=equipment_dict['option3'],
                                            option4=equipment_dict['option4'],
                                            user_id=user.user_id)
    
        db.session.add(equipment)
        db.session.commit()
    
    else:
        equipment=dndcrud.create_equipment(option1=equipment_dict['option1'],
                                            option2=equipment_dict['option2'],
                                            option3=equipment_dict['option3'],
                                            option4=equipment_dict['option4'],
                                            user_id=user.user_id)
    
        db.session.add(equipment)
        db.session.commit()

    ability_mod_con= (abilities.con-10)//2
    ability_mod_dex= (abilities.dex-10)//2

    hit_points=ability_mod_con+10
    proficiency_bonus= 2
    speed=30
    initiative=ability_mod_dex

    check_otherstats=dndcrud.get_otherstats_info(user.user_id)
    
    if check_otherstats is not None:
        otherstats= dndcrud.update_otherstats(proficiency_bonus=proficiency_bonus, 
                                          armor_class=armor_class, 
                                          hit_points=hit_points, 
                                          initiative= initiative, 
                                          speed=speed, user_id=user.user_id)
        
        db.session.add(otherstats)
        db.session.commit()
        
    else:
        otherstats= dndcrud.create_otherstats(proficiency_bonus=proficiency_bonus, 
                                          armor_class=armor_class, 
                                          hit_points=hit_points, 
                                          initiative= initiative, 
                                          speed=speed, user_id=user.user_id)

        db.session.add(otherstats)
        db.session.commit()



    return redirect ('/equipment')



@app.route('/otherstats')
def otherstats():


    return render_template('otherstats.html')



@app.route('/csheet')
def show_sheet():
    #TODO: get user_id from a get or post request
    user=dndcrud.get_user_info(session['current_user'])
    namefield=dndcrud.get_cnamefield_info(session['current_user'])
    abilities=dndcrud.get_abilities_info(session['current_user'])
    skills=dndcrud.get_skills_info(session['current_user'])
    equipment=dndcrud.get_equipment_info(session['current_user'])
    feats=dndcrud.get_feats_info(session['current_user'])

    otherstats=dndcrud.get_otherstats_info(session['current_user'])
    
    return render_template('csheet.html', 
                           user=user, 
                           namefield=namefield, 
                           abilities=abilities, 
                           skills=skills,
                           otherstats=otherstats,
                           equipment=equipment,
                           feats=feats)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
