from functools import wraps
from flask import Flask, session, redirect, url_for, render_template, flash
from contacto import contacto_bp
from autenticacion import autenticacion_bp
from conferencias import conferencias_bp
from notificaciones import notificaciones_bp
from evaluaciones import evaluaciones_bp
from asistente_bp import asistente_bp  # Blueprint del asistente
from orador_bp import orador_bp  # Blueprint del orador
from organizador_bp import organizador_bp  # Blueprint del organizador

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necesario para usar flash messages

# Registrar Blueprints
app.register_blueprint(contacto_bp)
app.register_blueprint(autenticacion_bp)
app.register_blueprint(conferencias_bp)
app.register_blueprint(notificaciones_bp)
app.register_blueprint(evaluaciones_bp)
app.register_blueprint(asistente_bp)
app.register_blueprint(orador_bp)
app.register_blueprint(organizador_bp)

# Decorador para verificar si el usuario ha iniciado sesión
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Por favor, inicia sesión para acceder a esta página", "warning")
            return redirect(url_for('autenticacion_bp.login'))
        return f(*args, **kwargs)
    return decorated_function

# Decorador para verificar el rol del usuario
def role_required(allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'role' not in session:
                flash("Acceso denegado. Inicia sesión para continuar.", "warning")
                return redirect(url_for('autenticacion_bp.login'))
            if session['role'] not in allowed_roles:
                flash("No tienes permiso para acceder a esta página.", "danger")
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Rutas protegidas según el rol

@app.route('/asistente/dashboard')
@login_required
@role_required(['asistente'])
def dashboard_asistente():
    return render_template('index.html')

@app.route('/orador/dashboard')
@login_required
@role_required(['orador'])
def dashboard_orador():
    return render_template('indexOR.html')

@app.route('/organizador/dashboard')
@login_required
@role_required(['organizador'])
def dashboard_organizador():
    return render_template('indexO.html')

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre_nosotros')
def sobre_nosotros():
    return render_template('nosotros.html')

@app.route('/programa')
def programa():
    # Llamar a la función que obtiene las conferencias
    lista_conferencias = obtener_conferencias()
    # Renderizar la plantilla y pasarle la lista de conferencias
    return render_template('programa.html', conferencias=lista_conferencias)

@app.route('/salas')
def salas():
    return render_template('salas.html')

@app.route('/diapositivas')
@login_required
@role_required(['asistente', 'orador', 'organizador'])  # Usuarios permitidos
def diapositivas():
    return render_template('diapositiva.html')

@app.route('/votacion')
@login_required
@role_required(['asistente', 'orador', 'organizador'])
def votacion():
    return render_template('votacion.html')

@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('inicio_sesion.html')

if __name__ == '__main__':
    app.run(debug=True)
