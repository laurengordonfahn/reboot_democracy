from sqlalchemy import func
#import all classes from model.py to enable funcitons to run here
from model import User
from model import Image



from model import connect_to_db, db
from curious import app, bcrypt
