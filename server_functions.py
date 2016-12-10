from model import *
from flask import (Flask, render_template, redirect, request, flash, session, jsonify)
from flask_bcrypt import Bcrypt
# to access regex for pattern matching for verifcation of email etc
import re


def current_user():
    """ Return the user object if in session """
    if 'current_user' in session:
        return User.query.get(session['current_user'])
    else:
        return None