from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session, jsonify)

from flask_debugtoolbar import DebugToolbarExtension

from flask_bcrypt import Bcrypt
import json

#for env variables
import os

#Need to create and import Classes in Database model.py
#ADD ALL CLASSES FROM MODELS!
from model import  *
# needed for communicating with API servers
import requests
# to access regex for pattern matching for verifcation of email etc
import re

#document containing api requests 
#use pattern below for any files made in same directory:
# import api_function_file_title

from server_functions import * #current_user()


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "Team Power Stance"

# value of key from shell environment
apikey=os.environ["GMJSAPIKEY"]

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined
#Fix server-side caching issues
app.jinja_env.auto_reload = True



from sqlalchemy.ext.declarative import DeclarativeMeta
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

#####PLACE ALL ROUTES HERE######

@app.route('/')
def index():
    """ Render Sign-In page """
    return render_template('index.html', 
                            apikey=apikey, 
                            current_user=current_user())

@app.route('/user_locations')
def user_locations():
    all_args = request.args.to_dict()
    print(all_args)

    date = all_args['date']
    min_lat = all_args['min_lat']
    min_long = all_args['min_long']
    max_lat = all_args['max_lat']
    max_long = all_args['max_long']

    result = db.session.query(User, Location).join(Location).all()
    results = map(lambda x: json.dumps(x, cls=AlchemyEncoder), result)
    return jsonify(results)
    # return json.dumps(result[3], cls=AlchemyEncoder)
    # return json.dumps([dict(r) for r in result])
    # print info

    # return jsonify(r)

def to_json(model):
    """ Returns a JSON representation of an SQLAlchemy-backed object.
    """
    json = {}
    json['fields'] = {}
    json['pk'] = getattr(model, 'id')

    for col in model._sa_class_manager.mapper.mapped_table.columns:
        json['fields'][col.name] = getattr(model, col.name)

    return dumps([json])

@app.route('/sign_up')
def sign_up():
    """ Render Sign-Up page"""
    return render_template('sign_up.html', current_user=current_user())


@app.route('/profile')
def profile():
    """ Render profile page"""
    return render_template('profile.html', current_user=current_user())




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # app.debug = False

    # Once I have a db I must activate this
    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    
    app.run(host="0.0.0.0",port=5000)
