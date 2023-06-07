
from dndmodel import db, User, Cnamefield, Abilities, Skills, Equipment, Otherstats, Feats


def create_user(email, user_name, password):
    """Create and return a new user."""

    user = User(email=email, user_name=user_name, password=password)

    return user


def get_user_info(user_id):
    """the function to show the character sheet"""

    user=User.query.filter(User.user_id==user_id).one() 
    
    return user

def get_cnamefield_info(user_id):
    """the function to show the character sheet"""

    namefield=Cnamefield.query.filter(Cnamefield.user_id==user_id).one() 
    
    return namefield


def get_abilities_info(user_id):
    """the function to show the character sheet"""

    abilities=Abilities.query.filter(Abilities.user_id==user_id).one() 
    
    return abilities

def get_skills_info(user_id):
    """the function to show the character sheet"""

    skills=Skills.query.filter(Skills.user_id==user_id).one() 
    
    return skills

def get_otherstats_info(user_id):
    """the function to show the character sheet"""

    otherstats=Otherstats.query.filter(Otherstats.user_id==user_id).one() 
    
    return otherstats

def get_equipment_info(user_id):
    """the function to show the character sheet"""

    equipment=Equipment.query.filter(Equipment.user_id==user_id).one() 
    
    return equipment

def get_feats_info(user_id):
    """the function to show the character sheet"""

    feat=Feats.query.filter(Feats.user_id==user_id).one() 
    
    return feat
