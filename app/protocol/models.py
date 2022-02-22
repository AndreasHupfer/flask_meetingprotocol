from app import db

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(32), index=True, nullable=False)
    date = db.DateTime(db.DateTime)
    time_begin = db.DateTime(db.Time)
    time_end = db.DateTime(db.Time)
    meetingParticipantRoles = db.relationship('MeetingParticipantRole', backref='meeting', lazy=True)

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    meetingParticipantRoles = db.relationship('MeetingParticipantRole', backref='participant', lazy=True)

class MeetingParticipantRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'))
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting.id'))

