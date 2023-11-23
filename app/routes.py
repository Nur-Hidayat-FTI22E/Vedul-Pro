from flask import render_template, redirect, url_for, flash
from app import app, db
from flask_login import login_user, current_user, logout_user, login_required
from app.model import User, Modul
from app.forms import FormDaftar, FormLogin

@app.route("/")
@app.route("/index")
def index():
    return render_template("tampilan_utama/index.html")


@app.route("/login", methods=['GET','POST'])
def login():
    form = FormLogin()
    if (current_user.is_authenticated):
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for("home"))
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/daftar", methods=['GET','POST'])
def daftar():
    form = FormDaftar()
    if (current_user.is_authenticated):
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data)
        if user is not None and form.password.data == form.password_lagi.data:
            newUser = User(namalengkap=form.namalengkap.data,username=form.username.data, hp=form.hp.data , email=form.email.data)
            newUser.set_password(form.password.data)
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for('login'))
        # print(form.email.data)
        # print(form.password.data)
        # print(form.password_lagi.data)
    return render_template("daftar.html",form=form)

@app.route("/modul")
@login_required
def modul():
    daftar_modul = Modul.query.all()
    return render_template("modul.html", daftar_modul=daftar_modul)

@app.route("/riwayat-pembelajaran")
@login_required
def riwayatpembelajaran():
    return render_template("riwayat_belajar.html")

@app.route("/help-&-support")
@login_required
def helpandsupport():
    return render_template("help&support/index.html")

@app.route("/home")
@login_required
def home():
    # print(f"[INFO] {current_user.}")
    return render_template("halaman-home/index.html")

@app.route("/Profile")
@login_required
def profile():
    return render_template("halaman_profil/index.html")

@app.route("/Checkout/<modulname>")
@login_required
def checkout(modulname):
    modul = Modul.query.filter_by(namamodul=modulname).first()
    return render_template("halaman_checkout/checkout.html",modul=modul)

@app.route("/marvel12")
def marvel12():
    return render_template("halaman_admin/index.html")

@app.route("/marvel12/data")
def data():
    return render_template("halaman_admin/data.html")