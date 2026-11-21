

from flask import render_template, redirect, url_for, flash, abort
from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from . import db
from .models import User, Competition
from .forms import RegistrationForm, LoginForm, CompetitionForm


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

    # US2: Organizer views their competitions
    @app.route("/competitions")
    @login_required
    def competitions():
        if current_user.role != "organizer":
            abort(403)

        my_competitions = Competition.query.filter_by(
            organizer_id=current_user.id
        ).order_by(Competition.start_date).all()

        return render_template(
            "competitions.html",
            competitions=my_competitions
        )

    # US3: Organizer creates a competition
    @app.route("/competitions/create", methods=["GET", "POST"])
    @login_required
    def create_competition():
        if current_user.role != "organizer":
            abort(403)

        form = CompetitionForm()

        if form.validate_on_submit():
            competition = Competition(
                name=form.name.data.strip(),
                description=form.description.data.strip(),
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                organizer_id=current_user.id
            )

            db.session.add(competition)
            db.session.commit()

            flash("Competition created successfully!")
            return redirect(url_for("competitions"))

        return render_template(
            "create_competition.html",
            form=form
        )
