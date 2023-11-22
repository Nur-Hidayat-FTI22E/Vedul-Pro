from app import app, db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    namalengkap = db.Column(db.String(30))
    email = db.Column(db.String(35))
    password_hash = db.Column(db.String(163))
    def __repr__(self):
        return f"<User {self.namalengkap}>"
    def set_password(self, passwd):
        self.password_hash = generate_password_hash(passwd)
    def check_password(self, passwd):
        return check_password_hash(self.password_hash, passwd)
 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    