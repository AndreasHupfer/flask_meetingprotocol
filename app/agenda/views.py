from flask import Blueprint, render_template
from app.models import Agenda

agenda = Blueprint('agenda', __name__)

@agenda.route('/')
def agendas():
    agendas = Agenda.query.order_by(Agenda.sorting).all()
    return render_template('agendas.html', title='Agendas', agendas=agendas)