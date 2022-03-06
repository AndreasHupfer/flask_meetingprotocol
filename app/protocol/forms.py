from flask_wtf import Form
from wtforms import StringField, DateField, DateTimeLocalField
from wtforms.validators import DataRequired


class MeetingForm(Form):
    subject = StringField('subject', validators=[DataRequired()])
    date = DateField('Meeting Date', validators=[DataRequired()], format='%m.%d.%Y')
    time_begin = DateTimeLocalField('Meeting Start', format='%m.%d.%Y %H.%M.%S')
    time_end = DateTimeLocalField('Meeting End', format='%m.%d.%Y %H.%M.%S')
