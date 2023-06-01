from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__='user'

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
    char_name= db.Column(db.VARCHAR(30))
    background = db.Column(db.VARCHAR(25))
    alignment = db.Column(db.VARCHAR(2))
    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)

    user = db.relationship('User', uselist=False, back_populates = "namefield")

    def __repr__(self):
        return f"<Character name={self.char_name} alignment={self.alignment}>"
    

class Attributes(db.Model):

    __tablename__='attributes'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    con = db.Column(db.Integer)
    int = db.Column(db.Integer)
    wis = db.Column(db.Integer)
    cha = db.Column(db.Integer)

    user = db.relationship('User', uselist=False , back_populates = "attributes")

    def __repr__(self):
        return f"<Attribute strength={self.strn} cha={self.cha}>"
    

class Skills(db.Model):

    """
    proficinecy starts at 2
    """
    __tablename__='skills'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    acrobatics = db.Column(db.Boolean)
    animal_handling = db.Column(db.Boolean)
    arcana = db.Column(db.Boolean)
    athletics = db.Column(db.Boolean)
    deception = db.Column(db.Boolean)
    history = db.Column(db.Boolean)
    insight = db.Column(db.Boolean)
    intimidation = db.Column(db.Boolean)
    investigation = db.Column(db.Boolean)
    medicine = db.Column(db.Boolean)
    nature = db.Column(db.Booblean)
    perception = db.Column(db.Boolean)
    performance = db.Column(db.Boolean)
    persuasion = db.Column(db.Boolean)
    religion = db.Column(db.Boolean)
    sleightoh = db.Column(db.Boolean)
    stealth = db.Column(db.Boolean)
    survival = db.Column(db.Boolean)

    user = db.relationship('User', uselist=False, back_populates = "skills")



class Otherstats(db.Model):

    __tablename__='otherstats'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    proficiency_bonus=db.Column(db.Integer)
    armor_class = db.Column(db.Integer)
    hit_points = db.Column(db.Integer)
    initative = db.Column(db.Integer)
    speed = db.Column(db.Integer)

    users = db.relationship('User', uselist=False, back_populates = "otherstats")

class Equipment(db.Model):

    __tablename__='equipment'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    armor = db.Column(db.VARCHAR(25))
    weapons = db.Column(db.VARCHAR(25))
    potion = db.Column(db.VARCHAR(25))
    ring = db.Column(db.VARCHAR(25))

    users = db.relationship('User', back_populates = "equipment")

class Feats(db.Model):

    __tablename__='feats'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    feat1 = db.Column(db.VARCHAR(50))
    feat2 = db.Column(db.VARCHAR(50))

    users = db.relationship('User', back_populates = "feats")

def connect_to_db(flask_app, db_uri="postgresql:///dnd-learn", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from dndserver import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
