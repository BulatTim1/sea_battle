from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    # remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('Sign in')


class RegForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    repassword = PasswordField('repassword', validators=[DataRequired()])
    submit = SubmitField('Sign up')


class SetShip(FlaskForm):
    c = SelectField('Char for ship', validators=[DataRequired()],
                    choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'),
                             ('H', 'H'), ('I', 'I'), ('J', 'J')])
    d = SelectField('Digit for ship', validators=[DataRequired()],
                    choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                             ('8', '8'), ('9', '9'), ('10', '10')])
    p = SelectField("Ship's position", validators=[DataRequired()],
                    choices=[('Horizontally', 'Horizontally'), ('Vertically', 'Vertically')])
    submit = SubmitField('Submit')


class SetHit(FlaskForm):
    c = SelectField('Char for ship', validators=[DataRequired()],
                    choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'),
                             ('H', 'H'), ('I', 'I'), ('J', 'J')])
    d = SelectField('Digit for ship', validators=[DataRequired()],
                    choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                             ('8', '8'), ('9', '9'), ('10', '10')])
    submit = SubmitField('Submit')
