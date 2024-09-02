from flask import Flask, render_template
from contacto import contacto_bp
from autenticacion import autenticacion_bp
from conferencias import conferencias_bp
from notificaciones import notificaciones_bp
from evaluaciones import evaluaciones_bp

app = Flask(__name__,
            template_folder="../Frontend/templates",
            static_folder="../Frontend/static")

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

if __name__ == '__main__':
    app.run(debug=True)
