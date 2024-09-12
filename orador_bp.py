from flask import Blueprint, render_template

# Definir el Blueprint del orador
orador_bp = Blueprint('orador_bp', __name__)

# Ruta para la página de inicio
@orador_bp.route('/indexOR')
def indexOR():
    return render_template('./orador/indexOR.html')

# Ruta para la página de charlas
@orador_bp.route('/panel')
def panel():
    return render_template('./orador/panel.html')

# Ruta para la página de subir diapositivas
@orador_bp.route('/subirdiapo')
def subirdiapo():
    return render_template('./orador/subirdiapo.html')

# Ruta para la página de perfil
@orador_bp.route('/perfil')
def perfil():
    return render_template('./orador/perfil.html')

# Ruta para la página de revisiones de evaluaciones
@orador_bp.route('/revisarEva')
def revisarEva():
    return render_template('./orador/revisarEva.html')
