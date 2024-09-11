from flask import Blueprint, render_template

asistente_bp = Blueprint('asistente_bp', __name__)

@asistente_bp.route('/dashboard_asistente')
def dashboard_asistente():
    return render_template('index.html')
