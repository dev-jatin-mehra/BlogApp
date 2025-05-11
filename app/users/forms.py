from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,ValidationError,Email,Length,EqualTo
from flask_login import current_user
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password',
                                    validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):

        user = User.query.filter_by(username = username.data).first()      # doubt in this line 
        if user:
            raise ValidationError('Username is Taken ! Please Choose a different One !')
        
    def validate_email(self,email):

        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('An account is already registered with this email !')

class LogInForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit=SubmitField('LogIn')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','jpeg','png'])])

    submit=SubmitField('update')

    def validate_username(self,username):

        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('Username is Taken ! Please Choose as Different One !')
        
    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('An account is already registered with this email !')
            

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):

        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email ! Please register yourself !')
    

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password',
                                    validators=[DataRequired(),EqualTo('password')])
    
    submit = SubmitField('Change Password')        