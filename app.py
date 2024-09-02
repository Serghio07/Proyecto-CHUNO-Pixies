from flask import Flask, render_template
from contacto import contacto_bp
from autenticacion import autenticacion_bp
from conferencias import conferencias_bp
from notificaciones import notificaciones_bp
from evaluaciones import evaluaciones_bp

app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(contacto_bp)
app.register_blueprint(autenticacion_bp)
app.register_blueprint(conferencias_bp)
app.register_blueprint(notificaciones_bp)
app.register_blueprint(evaluaciones_bp)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para "Sobre Nosotros"
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

# Ruta para "Servicios"
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

# Ruta para "Contacto"
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Ruta para "Panel Orador"
@app.route('/orador_panel')
def orador_panel():
    return render_template('orador_panel.html')

# Ruta para "Panel Asistente"
@app.route('/asistente_panel')
def asistente_panel():
    return render_template('asistente_panel.html')

# Ruta para "Panel Organizador"
@app.route('/organizador_panel')
def organizador_panel():
    return render_template('organizador_panel.html')

# Ruta para "Evaluaciones"
@app.route('/evaluacion')
def evaluacion():
    return render_template('evaluacion.html')

if __name__ == '__main__':
    app.run(debug=True)
