from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app=Flask(__name__)
#local database
# TODO: change postgres path to your specific path (sql on your computer) and "DB_NAme" to db name
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:"postgres_"PASSWORD"@localhost/"DB_NAME"'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:PASSWORD@localhost/TicTacToe'
db=SQLAlchemy(app)

class Users(db.Model): # Create table "users" with all categories
    __tablename__= "users"

    uId=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    first_name=db.Column(db.String(120))
    last_name=db.Column(db.String(120))
    gender_=db.Column(db.String(120))
    age_=db.Column(db.Integer)

    def __init__(self, uId,email_, first_name, last_name, gender_, age_):
        self.uId = uId
        self.email_ = email_
        self.first_name = first_name
        self.last_name = last_name
        self.gender_ = gender_
        self.age_ = age_

class Games(db.Model): # Create table "games" with all categories and a foreign key from "users"
    __tablename__ = "games"

    game_number=db.Column(db.Integer, primary_key=True)
    user_=db.Column(db.Integer, ForeignKey('users.uId'))
    gameplay_=db.Column(db.String(5000))
    first_player=db.Column(db.String(10))
    result=db.Column(db.String(120))

    def __init__(self, game_number, user_, gameplay_, first_player, result):
        self.game_number = game_number
        self.user_ = user_
        self.gameplay_ = gameplay_
        self.first_player = first_player
        self.result = result

if __name__ == "__main__":
    # actually create the tables in already existing database
    db.create_all()
