from app import db

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






