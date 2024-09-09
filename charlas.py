from flask import Blueprint, request, jsonify
from firebase_admin import firestore

charlas_bp = Blueprint('charlas_bp', __name__)
db = firestore.client()

@charlas_bp.route('/charlas', methods=['POST'])
def crear_charla():
    datos = request.json
    try:
        db.collection('charlas').add(datos)
        return jsonify({"mensaje": "Charla creada exitosamente"}), 201
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@charlas_bp.route('/charlas', methods=['GET'])
def obtener_charlas():
    try:
        charlas = db.collection('charlas').get()
        lista_charlas = [charla.to_dict() for charla in charlas]
        return jsonify(lista_charlas), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@charlas_bp.route('/charlas/<id_charla>', methods=['PUT'])
def actualizar_charla(id_charla):
    datos = request.json
    try:
        db.collection('charlas').document(id_charla).update(datos)
        return jsonify({"mensaje": "Charla actualizada exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@charlas_bp.route('/charlas/<id_charla>', methods=['DELETE'])
def eliminar_charla(id_charla):
    try:
        db.collection('charlas').document(id_charla).delete()
        return jsonify({"mensaje": "Charla eliminada exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
