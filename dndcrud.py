
from dndmodel import db, User, Cnamefield, Abilities, Skills, Equipment, Otherstats, Feats


def create_user(email, user_name, password):
    """Create and return a new user."""

    user = User(email=email, user_name=user_name, password=password)

    return user




def get_user_info(user_id):
    

    user=User.query.filter(User.user_id==user_id).first() 
    
    return user

def get_user_by_email(email):
    user_email = User.query.filter(User.email == email).first()
    return user_email

def updating_cname(char_name, alignment, background, user_id):
    
    namefield=Cnamefield.query.filter(Cnamefield.user_id==user_id).first()

    

    namefield.char_name = char_name
    namefield.alignment = alignment
    namefield.background = background

    
    return namefield

def get_cnamefield_info(user_id):
    

    namefield=Cnamefield.query.filter(Cnamefield.user_id==user_id).first() 
    
    return namefield

def create_cnamefield_info(char_name, alignment, background, user_id):

    cname=Cnamefield(char_name=char_name, alignment=alignment, background=background, user_id=user_id)

    return cname


def get_abilities_info(user_id):
    

    abilities=Abilities.query.filter(Abilities.user_id==user_id).first() 
    
    return abilities

def updating_abilities(str, dex, con, int, wis, cha, user_id):
    
    abilities=Abilities.query.filter(Abilities.user_id==user_id).first()

    abilities.str=str
    abilities.dex=dex
    abilities.con=con
    abilities.int=int
    abilities.wis=wis
    abilities.cha=cha

    return abilities

def durable_feat(con, user_id):
    abilities=Abilities.query.filter(Abilities.user_id==user_id).first()

    abilities.con=con
    return abilities

def create_abilities(str, dex, con, int, wis, cha, user_id):

    ability_scores=Abilities(str=str, dex=dex, con=con, int=int, wis=wis, cha=cha, user_id=user_id)

    return(ability_scores)


def get_skills_info(user_id):
    

    skills=Skills.query.filter(Skills.user_id==user_id).first() 
    
    return skills

def create_skills(rskill, cskill1, cskill2, bskill1, bskill2,  user_id):
    

    the_skills=Skills(skill1=rskill, skill2=cskill1, skill3=cskill2, skill4=bskill1, skill5=bskill2, user_id= user_id)

    return the_skills

def update_skills(rskill, cskill1, cskill2, bskill1, bskill2,  user_id):
    

    the_skills=Skills.query.filter(Skills.user_id==user_id).first()

    the_skills.skill1=rskill
    the_skills.skill2=cskill1
    the_skills.skill3=cskill2
    the_skills.skill4=bskill1
    the_skills.skill5=bskill2

    return the_skills

def create_otherstats(proficiency_bonus, armor_class, hit_points, initiative, speed, user_id):

    otherstats=Otherstats(proficiency_bonus=proficiency_bonus,
                          armor_class=armor_class, 
                          hit_points=hit_points, 
                          initiative=initiative,
                          speed=speed,
                          user_id=user_id)
    return otherstats

def update_otherstats(proficiency_bonus, armor_class, hit_points, initiative, speed, user_id):

    otherstats=Otherstats.query.filter(Otherstats.user_id==user_id).first()

    otherstats.proficiency_bonus=proficiency_bonus
    otherstats.armor_class=armor_class
    otherstats.hit_points=hit_points
    otherstats.initiative=initiative
    otherstats.speed=speed

    return otherstats


def get_otherstats_info(user_id):
    

    otherstats=Otherstats.query.filter(Otherstats.user_id==user_id).first() 
    
    return otherstats

def create_equipment(option1, option2, option3, option4, user_id):

    equipment=Equipment(option1=option1, option2=option2, option3=option3, option4=option4, user_id=user_id)

    return equipment

def update_equipment(option1, option2, option3, option4, user_id):

    equipment=Equipment.query.filter(Equipment.user_id==user_id).first()
    equipment.option1=option1
    equipment.option2=option2
    equipment.option3=option3
    equipment.option4=option4

    return equipment

def get_equipment_info(user_id):
    

    equipment=Equipment.query.filter(Equipment.user_id==user_id).first() 
    
    return equipment

def create_feats(feat, fighting_style, user_id):

    feats=Feats(feat=feat, fighting_style=fighting_style, user_id=user_id)

    return feats

def update_feats(feat, fighting_style, user_id):
    

    feats=Feats.query.filter(Feats.user_id==user_id).first()

    feats.feat=feat
    feats.fighting_style=fighting_style


    return feats

def get_feats_info(user_id):
    

    feat=Feats.query.filter(Feats.user_id==user_id).first() 
    
    return feat
