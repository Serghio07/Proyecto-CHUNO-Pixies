from flask import Blueprint, request, jsonify
import firebase_admin
from firebase_admin import firestore

conferencias_bp = Blueprint('conferencias_bp', __name__)

db = firestore.client()

@conferencias_bp.route('/conferencias', methods=['POST'])
def crear_conferencia():
    datos = request.json
    try:
        db.collection('conferencias').add(datos)
        return jsonify({"mensaje": "Conferencia creada exitosamente"}), 201
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@conferencias_bp.route('/conferencias', methods=['GET'])
def obtener_conferencias():
    try:
        conferencias = db.collection('conferencias').get()
        lista_conferencias = [conf.to_dict() for conf in conferencias]
        return jsonify(lista_conferencias), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@conferencias_bp.route('/conferencias/<id_conferencia>', methods=['PUT'])
def actualizar_conferencia(id_conferencia):
    datos = request.json
    try:
        db.collection('conferencias').document(id_conferencia).update(datos)
        return jsonify({"mensaje": "Conferencia actualizada exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@conferencias_bp.route('/conferencias/<id_conferencia>', methods=['DELETE'])
def eliminar_conferencia(id_conferencia):
    try:
        db.collection('conferencias').document(id_conferencia).delete()
        return jsonify({"mensaje": "Conferencia eliminada exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
