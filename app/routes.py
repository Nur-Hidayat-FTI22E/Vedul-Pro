from flask import render_template, redirect, url_for, flash
from app import app, db
from flask_login import login_user, current_user, logout_user, login_required
from app.model import User
from app.forms import FormDaftar, FormLogin

@app.route("/")
@app.route("/index")
def index():
    return render_template("tampilan_utama/index.html")


@app.route("/login", methods=['GET','POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for("home"))
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/daftar", methods=['GET','POST'])
def daftar():
    form = FormDaftar()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data)
        if user is not None and form.password.data == form.password_lagi.data:
            newUser = User(namalengkap=form.namalengkap.data, email=form.email.data)
            newUser.set_password(form.password.data)
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for('login'))
        # print(form.email.data)
        # print(form.password.data)
        # print(form.password_lagi.data)
    return render_template("daftar.html",form=form)

@app.route("/modul")
def modul():
    return render_template("modul.html")

@app.route("/riwayat-pembelajaran")
def riwayatpembelajaran():
    return render_template("riwayat_belajar.html")

@app.route("/help-&-support")
def helpandsupport():
    return render_template("help&support/index.html")

@app.route("/home")
def home():
    # print(f"[INFO] {current_user.}")
    return render_template("halaman-home/index.html")

@app.route("/Profile")
def profile():
    return render_template("halaman_profil/index.html")