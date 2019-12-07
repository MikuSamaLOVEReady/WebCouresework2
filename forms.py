from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo
from wtforms import ValidationError
from ..models import User




class loginForm(FlaskForm):
    name = StringField('UserName',validators=[DataRequired()])
    password = StringField('Password',validators=[DataRequired()])
    submit =SubmitField('Log In')

class Regiser(FlaskForm):
    name = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('password2',message='Password not matched')])
    password2 = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')
    def validate_name(self, filed):
        if (User.query.filter_by(username=filed.data)).first():
            raise ValidationError('Username already used')




