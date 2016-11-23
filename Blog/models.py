
#_*_coding:UTF-8_*_
from Blog import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64),unique = True)
    # db.relationship()的第一个参数表明这个关系的另一端是哪个模型。如果模型类尚未定义，可使用字符串形式指定
    # backref参数向User模型中添加一个role属性，从而定义反向关系。这一属性可替代role_id访问Role模型，此时获取的是模型对象，而不是外键的值
    # lazy = 'dynamic'参数，从而禁止自动执行查询
    users = db.relationship('User',backref = 'role',lazy = 'dynamic')
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username



