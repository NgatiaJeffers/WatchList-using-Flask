from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required
from app.instance.config import SECRET_KEY

class ReviewForm(FlaskForm):

    title = StringField('Review title', validators = [Required()])
    review = TextAreaField('Movie review', validators = [Required()])
    submit = SubmitField('Submit')  