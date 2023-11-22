from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Email, DataRequired

class FormLogin(FlaskForm):
    email = EmailField("Email")
    password = PasswordField("Password")
    submit = SubmitField("Login")


class FormDaftar(FlaskForm):
    namalengkap = StringField("Nama Lengkap", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password_lagi = PasswordField("Ulangi Password", validators=[DataRequired()])
    submit = SubmitField("Register")
