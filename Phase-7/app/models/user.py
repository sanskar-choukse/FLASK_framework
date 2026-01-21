from flask_sqlalchemy import SQLALCHEMY

db=SQLALCHEMY()

class user(db.model):
    id=db.column(db.integer,primary_key=True)
    name=db.column(db.string(100),nullable=False)
    email=db.column(db.string(200),unique=True)
    posts=db.relationship('post',backref='author',lazy=True)