from flask_login import UserMixin
from app import db
from . import login_manager

userGame = db.Table('userGame',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('Game.id'))
)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ ='users'
    id = db.Column(db.Integer,primary_key = True)
    username =db.Column(db.String(25),unique=True,index=True)
    password =db.Column(db.String(30),index=True)
    game = db.relationship('Game',secondary=userGame)

class Game(db.Model):
    __tablename__ = 'Game'
    id =db.Column(db.Integer,primary_key = True)
    Gamename =db.Column(db.String(25),index=True)
    Price =db.Column(db.Float,index=True)
    #Customer_ID =db.Column(db.Integer,db.ForeignKey(User.id))
    #modules = db.relationship('Module', secondary=enrollment)
    buyer =db.relationship('User',secondary=userGame)  #User 可以通过 backref 获得游戏信息
