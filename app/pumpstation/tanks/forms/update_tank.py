from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length

from app.models.tank import Tank

class UpdateTankForm(FlaskForm):

    fullname = StringField('Fullname', validators=[DataRequired(), Length(min=6, max=10)])
    location = StringField('Location', validators=[DataRequired()])
    token = StringField('Token', validators=[])

    submit = SubmitField('Sign In')

    def set_tank_id(self,id):
        self.tank_id = id

    def validate_token(self, token):          
        tank = Tank.query.filter_by(token=token.data).first()

        if tank != None:            
            if tank.id != self.tank_id:
                raise ValidationError('Sorry my Friend, this token is in use')