
from dndmodel import db, User, Cnamefield, Abilities, Skills, Equipment, Otherstats, Feats


def create_user(email, user_name, password):
    """Create and return a new user."""

    user = User(email=email, user_name=user_name, password=password)

    return user




def get_user_info(user_id):
    

    user=User.query.filter(User.user_id==user_id).one() 
    
    return user

def get_user_by_email(email):
    user_email = User.query.filter(User.email == email).first()
    return user_email

def get_cnamefield_info(user_id):
    

    namefield=Cnamefield.query.filter(Cnamefield.user_id==user_id).one() 
    
    return namefield

def create_cnamefield_info(char_name, alignment, background, user_id):

    cname=Cnamefield(char_name=char_name, alignment=alignment, background=background, user_id=user_id)

    return cname


def get_abilities_info(user_id):
    

    abilities=Abilities.query.filter(Abilities.user_id==user_id).one() 
    
    return abilities

def create_abilities(str, dex, con, int, wis, cha, user_id):

    ability_scores=Abilities(str=str, dex=dex, con=con, int=int, wis=wis, cha=cha, user_id=user_id)

    return(ability_scores)


def get_skills_info(user_id):
    

    skills=Skills.query.filter(Skills.user_id==user_id).one() 
    
    return skills

def get_otherstats_info(user_id):
    

    otherstats=Otherstats.query.filter(Otherstats.user_id==user_id).one() 
    
    return otherstats

def get_equipment_info(user_id):
    

    equipment=Equipment.query.filter(Equipment.user_id==user_id).one() 
    
    return equipment

def get_feats_info(user_id):
    

    feat=Feats.query.filter(Feats.user_id==user_id).one() 
    
    return feat
