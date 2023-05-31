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

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

class Cnamefield(db.Model):

    __tablename__ = 'namefield'
    """
    for this build, lvl is 1, race is human, variant human, class is fighter


    """
    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'))
    char_name= db.Column(db.VARCHAR(30))
    background = db.Column(db.VARCHAR(25))
    alignment = db.Column(db.VARCHAR(2))

    users = db.relationship('User', back_populates = "equipment")

    def __repr__(self):
        return f"<Character name={self.char_name} alignment={self.alignment}>"
    

class Attributes(db.Model):

    __tablename__='attributes'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'))
    strn = db.Column(db.Integer)
    dex = db.Column(db.Integer)
    con = db.Column(db.Integer)
    int = db.Column(db.Integer)
    wis = db.Column(db.Integer)
    cha = db.Column(db.Integer)

    users = db.relationship('User', back_populates = "equipment")

    def __repr__(self):
        return f"<Attribute strength={self.strn} cha={self.cha}>"
    

class Skills(db.Model):

    """
    proficinecy starts at 2
    """
    __tablename__='skills'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'))
    acrobatics = db.Column(db.VARCHAR(1))
    animal_handling = db.Column(db.VARCHAR(1))
    arcana = db.Column(db.VARCHAR(1))
    athletics = db.Column(db.VARCHAR(1))
    deception = db.Column(db.VARCHAR(1))
    history = db.Column(db.VARCHAR(1))
    insight = db.Column(db.VARCHAR(1))
    intimidation = db.Column(db.VARCHAR(1))
    investigation = db.Column(db.VARCHAR(1))
    medicine = db.Column(db.VARCHAR(1))
    nature = db.Column(db.VARCHAR(1))
    perception = db.Column(db.VARCHAR(1))
    performance = db.Column(db.VARCHAR(1))
    persuasion = db.Column(db.VARCHAR(1))
    religion = db.Column(db.VARCHAR(1))
    sleightoh = db.Column(db.VARCHAR(1))
    stealth = db.Column(db.VARCHAR(1))
    survival = db.Column(db.VARCHAR(1))

    users = db.relationship('User', back_populates = "equipment")

    def __repr__(self):
        return f"<Character name={self.c} alignment={self.alignment}>"

class Otherstats(db.Model):

    __tablename__='otherstats'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'))
    proficiency_bonus=db.Column(db.Integer)
    armor_class = db.Column(db.Integer)
    hit_points = db.Column(db.Integer)
    initative = db.Column(db.Integer)
    speed = db.Column(db.Integer)

    users = db.relationship('User', back_populates = "equipment")

class Equipment(db.Model):

    __tablename__='equipment'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'))
    armor = db.Column(db.VARCHAR(25))
    weapons = db.Column(db.VARCHAR(25))
    potion = db.Column(db.VARCHAR(25))
    ring = db.Column(db.VARCHAR(25))

    users = db.relationship('User', back_populates = "equipment")

class Feats(db.Model):

    __tablename__='feats'

    feat1 = db.Column(db.VARCHAR(50))
    feat2 = db.Column(db.VARCHAR(50))

    users = db.relationship('User', back_populates = "equipment")


