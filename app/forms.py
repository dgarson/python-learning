# flask_tracking/users/forms.py
from flask_wtf import Form
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from wtforms.fields import StringField
from wtforms.validators import Email, InputRequired, ValidationError

from app.models import Account

class LoginForm(Form):
    email = StringField(validators=[InputRequired(), Email()])
    password = StringField(validators=[InputRequired()])
    error = ValidationError()

    # WTForms supports "inline" validators
    # which are methods of our `Form` subclass
    # with names in the form `validate_[fieldname]`.
    # This validator will run after all the
    # other validators have passed.
    def validate_password(_self, field):
        try:
            user = Account.query.filter(Account.email == _self.email.data).one()
        except (MultipleResultsFound, NoResultFound):
            raise ValidationError("Invalid user")
        if user is None:
            raise ValidationError("Invalid user")
        if not user.is_valid_password(_self.password.data):
            raise ValidationError("Invalid password")

        # Make the current user available
        # to calling code.
        _self.user = user


class RegistrationForm(Form):
    name = StringField("Display Name")
    email = StringField(validators=[InputRequired(), Email()])
    password = StringField(validators=[InputRequired()])

    def validate_email(_self, field):
        _self.user = Account.query.filter(Account.email == field.data).first()
        if _self.user is not None:
            raise ValidationError("A user with that email already exists")

