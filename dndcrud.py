
from dndmodel import db, User

def create_user(email, user_name, password):
    """Create and return a new user."""

    user = User(email=email, user_name=user_name, password=password)

    return user


def get_user_info(user_id):
    """the function to show the character sheet"""

    user=User.query.filter(User.user_id==user_id).one() 
    
    return user

def get_Cnamefield_info(user_id):
    """the function to show the character sheet"""

    namefield=Cnamefield.query.filter(Cnamefield.user_id==user_id).one() 
    
    return namefield

