
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import db
from .models import User
from .forms import RegistrationForm, LoginForm


def register_routes(app):

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        form = RegistrationForm()

        if form.validate_on_submit():
            user = User(
                name=form.name.data,
                email=form.email.data.strip().lower(),
                role=form.role.data
            )

            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()

            flash("Registration successful!")
            return redirect(url_for("login"))

        return render_template("register.html", form=form)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        form = LoginForm()

        if form.validate_on_submit():
            email = form.email.data.strip().lower()
            user = User.query.filter_by(email=email).first()

            if user and user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for("index"))

            flash("Invalid email or password.")

        return render_template("login.html", form=form)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("index"))
