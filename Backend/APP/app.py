from flask import Flask
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

if __name__ == '__main__':
    app.run(debug=True)
