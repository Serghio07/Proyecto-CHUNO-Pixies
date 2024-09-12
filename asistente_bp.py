from flask import Blueprint, render_template

asistente_bp = Blueprint('asistente_bp', __name__)

@asistente_bp.route('/dashboard1')
def dashboard1():
    return render_template('index.html')
