from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    gpx = FileField('Upload GPX file', validators=[FileAllowed(['gpx'])])
    submit = SubmitField('Post')
    
    # gpx = FileField('Upload GPX file', validators=[
    #      FileRequired(),
    #      FileAllowed(['gpx'], 'GPX files only!')
    #  ])

class UpdatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    gpx = FileField('Upload GPX file', validators=[FileAllowed(['gpx'])])
    gpx_submit = SubmitField('Update GPX file')
    submit = SubmitField('Update')