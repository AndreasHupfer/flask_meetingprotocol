from app import db

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(32), index=True, nullable=False)
    date_time_begin = db.Column(db.DateTime)
    date_time_end = db.Column(db.DateTime)
    meetingParticipantRoles = db.relationship('MeetingParticipantRole', backref='meeting', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

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

class Agenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sorting = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(32), index=True)
    type = db.Column(db.String(16), index=True, nullable=False)
    content = db.Column(db.Text(255))


