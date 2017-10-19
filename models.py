#encoding:utf-8

from app import db

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    # openid = db.Column(db.String(50))
    wechatid = db.Column(db.String(50))
    material = db.relationship('Material', backref='user', lazy='dynamic')
    article = db.relationship('Article', backref='user', lazy='dynamic')

class Material(db.Model):
    __tablename__ = 'material'
    mater_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    user_id =  db.Column(db.Integer, db.ForeignKey('user.user_id'),nullable=False)
    tag = db.Column(db.String(20),nullable=False)
    edit_time = db.Column(db.DateTime,nullable=False)

class Article(db.Model):
    __tablename__ = "article"
    artic_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(20),nullable=False)
    content = db.Column(db.Text,nullable=False)
    user_id =  db.Column(db.Integer, db.ForeignKey('user.user_id'),nullable=False)
    edit_time = db.Column(db.DateTime,nullable=False)
