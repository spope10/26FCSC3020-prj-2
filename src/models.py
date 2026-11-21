
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


class Competition(db.Model):
    __tablename__ = "competitions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    organizer_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    organizer = db.relationship(
        "User",
        backref="competitions"
    )


class Challenge(db.Model):
    __tablename__ = "challenges"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    flag = db.Column(db.String(255), nullable=False)

    competition_id = db.Column(
        db.Integer,
        db.ForeignKey("competitions.id"),
        nullable=False
    )

    competition = db.relationship(
        "Competition",
        backref="challenges"
    )


class Registration(db.Model):
    __tablename__ = "registrations"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    competition_id = db.Column(
        db.Integer,
        db.ForeignKey("competitions.id"),
        nullable=False
    )

    user = db.relationship(
        "User",
        backref="registrations"
    )

    competition = db.relationship(
        "Competition",
        backref="registrations"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "competition_id",
            name="unique_user_competition"
        ),
    )
