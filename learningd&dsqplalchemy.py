from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__='users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_name=db.Column(db.VARCHAR(25))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

class Cnamefield(db.Model):

    __tablename__ = "namefield"
    """
    for this build, lvl is 1, race is human, class is fighter


    """

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'))
    char_name= db.Column(db.VARCHAR(30))
    background = db.Column(db.VARCHAR(25))
    alignment = db.Column(db.VARCHAR(2))

class Attributes(db.Model):

    __tablename__='attributes'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'))
    strn = db.Column(db.Integer)
    dex = db.Column(db.Integer)
    con = db.Column(db.Integer)
    int = db.Column(db.Integer)
    wis = db.Column(db.Integer)
    cha = db.Column(db.Integer)
    

class Skills(db.Model):

    __tablename__='skills'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'))
    acrobatics = db.Column(db.Integer)
    animal_handling = db.Column(db.Integer)
    arcana = db.Column(db.Integer)
    athletics = db.Column(db.Integer)
    deception = db.Column(db.Integer)
    history = db.Column(db.Integer)
    insight = db.Column(db.Integer)
    intimidation = db.Column(db.Integer)
    investigation = db.Column(db.Integer)
    medicine = db.Column(db.Integer)
    nature = db.Column(db.Integer)
    perception = db.Column(db.Integer)
    performance = db.Column(db.Integer)
    persuasion = db.Column(db.Integer)
    religion = db.Column(db.Integer)
    sleightoh = db.Column(db.Integer)
    stealth = db.Column(db.Integer)
    survival = db.Column(db.Integer)



