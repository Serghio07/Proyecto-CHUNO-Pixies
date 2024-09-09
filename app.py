from flask import Flask, session, redirect, url_for, render_template, flash
from contacto import contacto_bp
from autenticacion import autenticacion_bp
from conferencias import conferencias_bp
from notificaciones import notificaciones_bp
from evaluaciones import evaluaciones_bp

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necesario para usar flash messages

# Registrar Blueprints
app.register_blueprint(contacto_bp)
app.register_blueprint(autenticacion_bp)
app.register_blueprint(conferencias_bp)
app.register_blueprint(notificaciones_bp)
app.register_blueprint(evaluaciones_bp)

# Decorador para verificar si el usuario ha iniciado sesión
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Por favor, inicia sesión para acceder a esta página", "warning")
            return redirect(url_for('autenticacion_bp.login'))
        return f(*args, **kwargs)
    return decorated_function

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
def diapositivas():
    if 'user' in session:
        return render_template('diapositiva.html', user=session['user'])
    else:
        flash("Por favor, inicia sesión para acceder a esta página", "warning")
        return redirect(url_for('autenticacion_bp.login'))

@app.route('/votacion')
def votacion():
    if 'user' in session:
        return render_template('votacion.html', user=session['user'])
    else:
        flash("Por favor, inicia sesión para acceder a esta página", "warning")
        return redirect(url_for('autenticacion_bp.login'))

@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('inicio_sesion.html')

if __name__ == '__main__':
    app.run(debug=True)
