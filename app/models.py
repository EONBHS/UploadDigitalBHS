from flask import Flask
from app import db



class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String)
    Profilepicture = db.Column(db.String)
    Password = db.Column(db.String)