from flask import Blueprint, render_template

organizador_bp = Blueprint('organizador_bp', __name__)

@organizador_bp.route('/dashboard_organizador')
def dashboard_organizador():
    return render_template('panel_principal.html')
