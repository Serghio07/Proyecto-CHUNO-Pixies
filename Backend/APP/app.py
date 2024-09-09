from flask import Flask
from autenticacion import autenticacion_bp
from conferencias import conferencias_bp
from notificaciones import notificaciones_bp
from evaluaciones import evaluaciones_bp
from charlas import charlas_bp
from salas import salas_bp
from personal import personal_bp
from panel_principal import panel_bp

app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(autenticacion_bp)
app.register_blueprint(conferencias_bp)
app.register_blueprint(notificaciones_bp)
app.register_blueprint(evaluaciones_bp)
app.register_blueprint(charlas_bp)
app.register_blueprint(salas_bp)
app.register_blueprint(personal_bp)
app.register_blueprint(panel_bp)

if __name__ == '__main__':
    app.run(debug=True)
