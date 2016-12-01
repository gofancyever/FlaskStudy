from app import db
from sqlalchemy import Integer,Column,String,ForeignKey,DateTime
from sqlalchemy.orm import relationship

from db_create import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer,primary_key=True)
    body = Column(String(140))
    timestamp = Column(DateTime)
    user_id = Column(Integer,ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
class User(Base):
    __tablename__ = "users"
    id = db.Column(Integer,primary_key=True)
    nickname = Column(String(64),index=True,unique=True)
    email = Column(String(120),index=True,unique=True)
    posts = relationship('Post',backref = 'author',lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)