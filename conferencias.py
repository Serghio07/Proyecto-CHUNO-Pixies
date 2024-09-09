from flask import Blueprint, render_template
from firebase_admin import firestore

# Crear el Blueprint para las rutas de conferencias
conferencias_bp = Blueprint('conferencias_bp', __name__)

# Inicializar Firestore (debes asegurarte de que Firestore está inicializado en tu aplicación)

db = firestore.client()

@conferencias_bp.route('/programa')
def programa():
    conferencias_ref = db.collection('conferencias')
    conferencias = conferencias_ref.stream()

    lista_conferencias = []
    for conferencia in conferencias:
        conferencia_data = conferencia.to_dict()
        lista_conferencias.append(conferencia_data)

    return render_template('programa.html', conferencias=lista_conferencias)
