from sqlalchemy import func
#import all classes from model.py to enable funcitons to run here
from model import User
from model import Image
from model import Location

from model import connect_to_db, db
from server import app, bcrypt
from faker import Factory
import random

fake=Factory.create()


def load_users():
    """ Load Users into Users Table"""

    User.query.delete()

    famous_list=[ "https://www.pexels.com/photo/blonde-haired-woman-in-blue-shirt-y-27411/", "https://www.pexels.com/photo/blonde-haired-woman-in-blue-shirt-y-27411/", "https://www.pexels.com/photo/man-wearing-blue-denim-buttons-up-long-sleeve-and-blace-frame-eyelgasses-26939/","https://www.pexels.com/photo/man-wearing-blue-denim-buttons-up-long-sleeve-and-blace-frame-eyelgasses-26939/", "https://www.pexels.com/photo/woman-in-white-v-neck-shirt-in-selective-focus-photography-157023/", "https://www.pexels.com/photo/man-sitting-next-to-couple-of-person-walking-on-the-street-during-daytime-211050/", "https://www.pexels.com/photo/light-person-woman-fire-5076/", "https://www.pexels.com/photo/woman-in-black-scoop-neck-shirt-smiling-38554/", "https://www.pexels.com/photo/summer-woman-nature-outdoors-108036/", "https://static.pexels.com/photos/108048/pexels-photo-108048.jpeg", "https://www.pexels.com/photo/2-person-and-1-child-connected-hands-159827/", "https://www.pexels.com/photo/sunglasses-trees-happy-glasses-58021/", "https://www.pexels.com/photo/woman-with-black-textile-87293/", "https://s3.amazonaws.com/uifaces/faces/twitter/zeldman/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/iannnnn/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/jsa/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/faulknermusic/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/sauro/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/zack415/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/k/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/brad_frost/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/abinav_t/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/ashleyford/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/adellecharles/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/kerem/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/jina/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/peterme/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/adhamdannaway/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/jm_denis/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/glif/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/tonypeterson/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/vista/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/mghoz/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/felipenogs/128.jpg", "https://s3.amazonaws.com/uifaces/faces/twitter/rem/128.jpg" ]

    for num in range(len(famous_list)):
        fname=fake.name().split(' ')[0]
        lname=fake.name().split(' ')[1]
        username=fname+lname
        email=fake.email()
        password=fake.password()
        profile_img=famous_list[num]

        person = User(fname=fname, lname=lname, username=username, email=email, password=password, profile_img=profile_img)
        db.session.add(person)
    db.session.commit()

def load_locations():
    """ Load the Locations from random generated data for demo"""

    

    Location.query.delete()
    #there are 36 users in the fake data for users
    orgin_x = 37.7811539
    orgin_y = -122.40799390000001
    maxRadius = .01

    origin = (orgin_x - maxRadius, orgin_y - maxRadius)

    for user in User.query.all():
        print(user.user_id)
        user_id=user.user_id

        randomPoint = (orgin_x + (random.random() * maxRadius * 2),
                       orgin_y + (random.random() * maxRadius * 2))
        location = Location(latitude=randomPoint[0], longitude=randomPoint[1], event_time="2016-01-20T09:00:00", user_id=user_id )
        db.session.add(location)
    db.session.commit()

        


def load_all():
    # Import different types of data
    load_users()
    load_locations()
    

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    load_all()
