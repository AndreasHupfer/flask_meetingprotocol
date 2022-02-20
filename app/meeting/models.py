from app import db

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(32), index=True, nullable=False)
    date = db.DateTime(db.DateTime)
    time_begin = db.DateTime(db.Time)
    time_end = db.DateTime(db.Time)
    meetingParticipantRoles = db.relationship('MeetingParticipantRole', backref='meeting', lazy=True)