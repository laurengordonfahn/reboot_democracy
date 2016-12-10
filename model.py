from flask_sqlalchemy import SQLAlchemy


# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()

# Helper functions

def connect_to_db(app,url='postgresql:///reboot_democracy'):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)
    app.config['SQLALCHEMY_ECHO'] = True




##### PLACE ALL CLASSES HERE FOR DB ########
class User(db.Model):
    __tablename__="users"

    user_id=db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    username=db.Column(db.String(50), nullable=False, unique=True)
    email=db.Column(db.String(100), nullable=False, unique=True)
    #large capasity for password due to encryption
    password=db.Column(db.String(128), nullable=False, unique=False)
    charity=db.Column(db.String(128))
    charity_url=db.Column(db.String(2083))
    address1=db.Column(db.String(500))
    address2=db.Column(db.String(100))
    city=db.Column(db.String(100))
    state=db.Column(db.String(2))
    zip_code=db.Column(db.Integer)
    profile_img=db.Column(db.String(2083))

class Image(db.Model):
    __tablename__="images"

    image_id=db.Column(db.Integer, 
                        primary_key=True,
                        autoincrement=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'))
    image_url=db.Column(db.String(2083)



if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from curious import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."