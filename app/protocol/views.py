import flask
from flask import Blueprint, render_template, url_for, redirect
from app.protocol.models import Meeting

protocol = Blueprint('protocol', __name__)


@protocol.route('/meetings')
def meetings():
    meetings = Meeting.query.order_by(Meeting.subject).all()
    return render_template('meetings.html', titel='Meetings', meetings=meetings)


@protocol.route('/meetings/<int:id>')
def meeting(id):
    meeting = Meeting.query.get_or_404(id)
    return render_template('meeting.html', titel='Meeting', meeting=meeting)

