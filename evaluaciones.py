from flask import Blueprint, request, jsonify
import firebase_admin
from firebase_admin import firestore

evaluaciones_bp = Blueprint('evaluaciones_bp', __name__)

db = firestore.client()

@evaluaciones_bp.route('/conferencias/<id_conferencia>/evaluar', methods=['POST'])
def evaluar_conferencia(id_conferencia):
    datos = request.json
    try:
        db.collection('conferencias').document(id_conferencia).collection('evaluaciones').add(datos)
        return jsonify({"mensaje": "Evaluación enviada exitosamente"}), 201
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@evaluaciones_bp.route('/conferencias/<id_conferencia>/evaluaciones', methods=['GET'])
def obtener_evaluaciones(id_conferencia):
    try:
        evaluaciones = db.collection('conferencias').document(id_conferencia).collection('evaluaciones').get()
        lista_evaluaciones = [eval.to_dict() for eval in evaluaciones]
        return jsonify(lista_evaluaciones), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
