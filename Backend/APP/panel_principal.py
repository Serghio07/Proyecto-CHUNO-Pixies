from flask import Blueprint, jsonify
from firebase_admin import firestore

panel_bp = Blueprint('panel_bp', __name__)
db = firestore.client()

@panel_bp.route('/estadisticas', methods=['GET'])
def obtener_estadisticas():
    try:
        asistentes = db.collection('asistentes').get()
        oradores = db.collection('oradores').get()
        salas_ocupadas = db.collection('salas').where('ocupada', '==', True).get()
        charlas = db.collection('charlas').get()

        estadisticas = {
            "asistentes": len(asistentes),
            "oradores": len(oradores),
            "salas_ocupadas": len(salas_ocupadas),
            "charlas_totales": len(charlas)
        }
        return jsonify(estadisticas), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
