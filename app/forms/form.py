from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

# RATING_CHOICES = ["G", "PG", "R"]

class NewTweetForm(FlaskForm):
    author = StringField("Author", validators=[DataRequired(), Length(max=50)])
    tweet = StringField("Tweet", validators=[DataRequired(),  Length(max=300)])
    # rating = SelectField("Rating", choices=RATING_CHOICES)
    submit = SubmitField("Create Tweet")
