
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

from .models import User


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])

    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8)]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password")]
    )

    role = SelectField(
        "Role",
        choices=[
            ("participant", "Participant"),
            ("organizer", "Organizer")
        ]
    )

    submit = SubmitField("Register")

    def validate_email(self, email):
        existing_user = User.query.filter_by(
            email=email.data.strip().lower()
        ).first()

        if existing_user:
            raise ValidationError("Email already registered.")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
