from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__='users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.VARCHAR(25), unique=True)
    user_name=db.Column(db.VARCHAR(25))
    password = db.Column(db.VARCHAR(25))

    namefield = db.relationship('Cnamefield', uselist=False, back_populates = "user")
    abilities = db.relationship('Abilities', uselist=False, back_populates = "user")
    skills = db.relationship('Skills', uselist=False, back_populates = "user")
    otherstats = db.relationship('Otherstats', uselist=False, back_populates = "user")
    equipment = db.relationship('Equipment', uselist=False, back_populates = "user")
    feats = db.relationship('Feats', uselist=False, back_populates = "user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email} user_name={self.user_name}>"

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
    

class Abilities(db.Model):

    __tablename__='abilities'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    str = db.Column(db.Integer)
    dex = db.Column(db.Integer)
    con = db.Column(db.Integer)
    int = db.Column(db.Integer)
    wis = db.Column(db.Integer)
    cha = db.Column(db.Integer)

    user = db.relationship('User', uselist=False , back_populates = "abilities")

    def __repr__(self):
        return f"<Ability strength={self.str} cha={self.cha}>"
    

class Skills(db.Model):

    """
    proficinecy starts at 2
    """
    __tablename__='skills'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    skill1=db.Column(db.VARCHAR)
    skill2=db.Column(db.VARCHAR)
    skill3=db.Column(db.VARCHAR)
    skill4=db.Column(db.VARCHAR)
    skill5=db.Column(db.VARCHAR)
    

    user = db.relationship('User', uselist=False, back_populates = "skills")



class Otherstats(db.Model):

    __tablename__='otherstats'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    proficiency_bonus=db.Column(db.Integer)
    armor_class = db.Column(db.Integer)
    hit_points = db.Column(db.Integer)
    initiative = db.Column(db.Integer)
    speed = db.Column(db.Integer)

    user = db.relationship('User', uselist=False, back_populates = "otherstats")

class Equipment(db.Model):

    __tablename__='equipment'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    option1 = db.Column(db.String)
    option2 = db.Column(db.String)
    option3 = db.Column(db.String)
    option4 = db.Column(db.String)
    

    user = db.relationship('User', back_populates = "equipment")

class Feats(db.Model):

    __tablename__='feats'

    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    feat = db.Column(db.VARCHAR(50))
    fighting_style = db.Column(db.VARCHAR(50))

    user = db.relationship('User', back_populates = "feats")

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
