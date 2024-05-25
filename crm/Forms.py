

from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField,PasswordField,SubmitField, ValidationError
from wtforms.validators import DataRequired,Email,EqualTo,Length
from flask_wtf.file import FileField,FileAllowed

from crmApp.models import User


class RegisterForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()]) 
    surname=StringField('Surname',validators=[DataRequired()])
    phonenumber=StringField('Phone number',validators=[DataRequired(),Length(min=10,max=10)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Condfirm Password',validators=[DataRequired(),EqualTo('password')])
    Submit=SubmitField('Register ')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            raise ValidationError('That email alread exists.')
        
    def validate_phoneno(self, phonenumber):
        user = User.query.filter_by(phone_number=self.phonenumber.data).first()
        if user:
            raise ValidationError('That phone number  alread exists.')

class LoginForm(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class TaskForm(FlaskForm):
    subject = StringField('module name',
                        validators=[DataRequired()])
    tasksdocs = FileField('upload doc')
    submit = SubmitField('upload')

