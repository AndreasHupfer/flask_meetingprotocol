from flask import Blueprint, render_template
from app.protocol.models import Meeting
from app.protocol.forms import MeetingForm

protocol = Blueprint('protocol', __name__)


@protocol.route('/meetings')
def meetings():
    meetings = Meeting.query.order_by(Meeting.subject).all()
    meeting = Meeting.query.get_or_404(1)
    return render_template('meetings.html', titel='Meetings', meetings=meetings, meeting=meeting)


@protocol.route('/meetings/<int:id>')
def meeting(id):
    meeting = Meeting.query.get_or_404(id)
    meetings = Meeting.query.order_by(Meeting.subject).all()
    return render_template('meetings.html', titel='Meeting', meeting=meeting, meetings=meetings)

@protocol.route('/meetings/add', methods=['GET', 'POST'])
def addMeeting():
    form = MeetingForm()
    return render_template('addMeeting.html', titel='Add Meeting', form=form)
