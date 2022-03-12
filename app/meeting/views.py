from flask import Blueprint, render_template
from app.models import Meeting
'''from app.meeting.forms import MeetingForm
import datetime'''

meeting = Blueprint('meeting', __name__)

@meeting.route('/')
def meetings():
    meetings = Meeting.query.order_by(Meeting.subject).all()
    meeting = Meeting.query.get_or_404(1)
    return render_template('meeting/meetings.html', title='Meetings', meetings=meetings, meeting=meeting)

@meeting.route('/meeting/post')
def meeting_post():
    pass


'''@meeting.route('/meetings/<int:id>')
def single_meeting(id):
    meeting = Meeting.query.get_or_404(id)
    meetings = Meeting.query.order_by(Meeting.subject).all()
    return render_template('meeting/meetings.html', title='Meeting', meeting=meeting, meetings=meetings)'''


'''@meeting.route('/meetings/add', methods=['GET', 'POST'])
def addMeeting():
    form = MeetingForm()
    if request.method == 'POST':
        m = Meeting(subject = request.form['subject'],
                    date_time_begin = datetime.datetime.strptime(request.form['time_begin'], '%Y-%m-%dT%H:%M'),
                    date_time_end = datetime.datetime.strptime(request.form['time_end'], '%Y-%m-%dT%H:%M'))
        print(datetime.datetime.strptime(request.form['time_begin'], '%Y-%m-%dT%H:%M'))
        m.insert()
    return render_template('meeting/addMeeting.html', title='Add Meeting', form=form)'''
