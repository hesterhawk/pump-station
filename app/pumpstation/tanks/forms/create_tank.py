from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

from app.models.tank import Tank

class CreateTankForm(FlaskForm):

    fullname = StringField('Fullname', validators=[DataRequired(), Length(min=6, max=10)])
    location = StringField('Location', validators=[DataRequired()])
    token = StringField('Token', validators=[DataRequired()])

    submit = SubmitField('Sign In')

    def validate_token(self, token):        
        tank = Tank.query.filter_by(token=token.data).first()

        if tank is not None:                
            raise ValidationError('Sorry my Friend, this token is in use')