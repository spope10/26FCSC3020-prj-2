
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SelectField,
    SubmitField,
    TextAreaField,
    DateTimeLocalField
)
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    EqualTo,
    ValidationError
)

from .models import User


class RegistrationForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired()]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8)]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password")
        ]
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
            raise ValidationError(
                "Email already registered."
            )


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")


class CompetitionForm(FlaskForm):
    name = StringField(
        "Competition Name",
        validators=[
            DataRequired(),
            Length(max=100)
        ]
    )

    description = TextAreaField(
        "Description",
        validators=[DataRequired()]
    )

    start_date = DateTimeLocalField(
        "Start Date and Time",
        format="%Y-%m-%dT%H:%M",
        validators=[DataRequired()]
    )

    end_date = DateTimeLocalField(
        "End Date and Time",
        format="%Y-%m-%dT%H:%M",
        validators=[DataRequired()]
    )

    submit = SubmitField(
        "Create Competition"
    )

    def validate_end_date(self, field):
        if self.start_date.data and field.data:
            if field.data <= self.start_date.data:
                raise ValidationError(
                    "End date must be after start date."
                )
