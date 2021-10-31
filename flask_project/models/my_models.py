from flask_project import db

class Note(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)

class Loggin_User(db.Model):
    __tablename__ = 'loggin_user_info'
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    passwd = db.Column(db.String(64))