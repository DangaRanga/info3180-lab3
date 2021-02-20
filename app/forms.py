"""This module contains the forms for the application."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import (
    InputRequired,
    DataRequired,
    Email,
    EqualTo,
    ValidationError,
    Length)


class ContactForm(FlaskForm):
    """Defines the contact form."""

    name = StringField('Name', validators=[
                       InputRequired(message="Please enter your name")
                       ])

    email = EmailField('Email Address', validators=[
                       Email(message='Please enter a valid email address'),
                       InputRequired(message='Please enter your email address')
                       ])
    subject = StringField('Subject', validators=[
                          InputRequired(message="Please enter the subject")])

    message_body = TextAreaField('Message Body', render_kw={
        "rows": 8, "cols": 50
    })
