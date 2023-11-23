from app import app, db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    namalengkap = db.Column(db.String(30))
    username = db.Column(db.String(25))
    hp = db.Column(db.String(20))
    email = db.Column(db.String(35))
    password_hash = db.Column(db.String(163))
    date_create_user = db.Column(db.DateTime, default=datetime.now())
    moduls = db.relationship('MyModul', backref='punya')
    def __repr__(self):
        return f"<User {self.namalengkap}>"
    def set_password(self, passwd):
        self.password_hash = generate_password_hash(passwd)
    def check_password(self, passwd):
        return check_password_hash(self.password_hash, passwd)
    
class Modul(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namamodul = db.Column(db.String(200))
    keterangan = db.Column(db.String(400))
    photo_path = db.Column(db.String(255))
    path_modul = db.Column(db.String(255))
    mo = db.relationship("MyModul", backref='dari')
    

class MyModul(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_modul = db.Column(db.ForeignKey(Modul.id))
    id_user = db.Column(db.ForeignKey(User.id))    
 


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    