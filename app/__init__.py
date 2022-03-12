from flask import Flask

import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config.Development)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
from app.meeting.views import meeting
from app.agenda.views import agenda

app.register_blueprint(meeting, url_prefix='/meeting')
app.register_blueprint(agenda, url_prefix='/agenda')