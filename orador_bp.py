from flask import Blueprint, render_template

orador_bp = Blueprint('orador_bp', __name__)

@orador_bp.route('/dashboard_orador')
def dashboard_orador():
    return render_template('panel.html')
