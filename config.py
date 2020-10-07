import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import app

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://zdangata:Smash1t1n@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False