from flask import Blueprint, render_template

organizador_bp = Blueprint('organizador_bp', __name__)

@organizador_bp.route('/dashboard3')
def dashboard3():
    return render_template('./organizador/indexO.html')
