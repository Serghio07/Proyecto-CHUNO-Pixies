from flask import Blueprint, request, jsonify
from firebase_admin import firestore

salas_bp = Blueprint('salas_bp', __name__)
db = firestore.client()

@salas_bp.route('/salas', methods=['POST'])
def crear_sala():
    datos = request.json
    try:
        db.collection('salas').add(datos)
        return jsonify({"mensaje": "Sala creada exitosamente"}), 201
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@salas_bp.route('/salas', methods=['GET'])
def obtener_salas():
    try:
        salas = db.collection('salas').get()
        lista_salas = [sala.to_dict() for sala in salas]
        return jsonify(lista_salas), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@salas_bp.route('/salas/<id_sala>', methods=['PUT'])
def actualizar_sala(id_sala):
    datos = request.json
    try:
        db.collection('salas').document(id_sala).update(datos)
        return jsonify({"mensaje": "Sala actualizada exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@salas_bp.route('/salas/<id_sala>', methods=['DELETE'])
def eliminar_sala(id_sala):
    try:
        db.collection('salas').document(id_sala).delete()
        return jsonify({"mensaje": "Sala eliminada exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
