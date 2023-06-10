
from flask import (Flask, render_template, request, flash, session,
                   redirect)
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
    user=dndcrud.get_user_info(session['current_user'])

    return render_template('cnamefield.html')

@app.route('/cnamefield-info', methods =['POST'] )
def add_namefield():
    user=dndcrud.get_user_info(session['current_user'])
    char_name = request.form.get('cname')
    alignment = request.form.get('alignment')
    background = request.form.get('backgrounds')
    


    namefield = dndcrud.create_cnamefield_info(char_name, alignment, background, user.user_id)
    db.session.add(namefield)
    db.session.commit()

  
    return redirect ('/cnamefield')

@app.route('/asnskills')
def asnskills():

    ability_scores=["str", "dex", "con", "int", "wis", "cha"]

    return render_template('asnskills.html', ability_scores=ability_scores)

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
            print(score_dict[ascore])

    abonus2=request.form.get('abonus2')
    for ascore in score_dict:
        if ascore==abonus1:
            score_dict[ascore]+=1
            print(score_dict[ascore])

    

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

    the_skills=dndcrud.create_skills(rskill=rskill,
                                     cskill1=cskill1,
                                     cskill2=cskill2,
                                     user_id=user.user_id)
    
    db.session.add(the_skills)
    db.session.commit()

    return redirect('asnskills.html')




@app.route('/otherstats')
def otherstats():


    return render_template('otherstats.html')





@app.route('/csheet')
def show_sheet():
    #TODO: get user_id from a get or post request
    user=dndcrud.get_user_info(1)
    namefield=dndcrud.get_cnamefield_info(1)
    abilities=dndcrud.get_abilities_info(1)
    skills=dndcrud.get_skills_info(1)
    otherstats=dndcrud.get_otherstats_info(1)
    equipment=dndcrud.get_equipment_info(1)
    feats=dndcrud.get_feats_info(1)
    #TODO: get user_id from a get or post request

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
