from flask import Blueprint, render_template
from app.meeting.models import Meeting

meeting = Blueprint('meeting', __name__)

@meeting.route('/meetings')
def meetings():
    meetings = Meeting.query.order_by(Meeting.subject).all()
    return render_template('meetings.html', titel='Meetings', meetings=meetings)


@meeting.route('/meeting/<id>')
def show_meeting(id):
    meeting = Meeting.query.get_or_404(id)
    return render_template('meeting.html', titel='Meeting', meeting=meeting)
