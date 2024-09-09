from flask import Blueprint, request, jsonify
from firebase_admin import firestore

personal_bp = Blueprint('personal_bp', __name__)
db = firestore.client()

@personal_bp.route('/personal', methods=['POST'])
def crear_personal():
    datos = request.json
    try:
        db.collection('personal').add(datos)
        return jsonify({"mensaje": "Personal agregado exitosamente"}), 201
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@personal_bp.route('/personal', methods=['GET'])
def obtener_personal():
    try:
        personal = db.collection('personal').get()
        lista_personal = [persona.to_dict() for persona in personal]
        return jsonify(lista_personal), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@personal_bp.route('/personal/<id_persona>', methods=['PUT'])
def actualizar_personal(id_persona):
    datos = request.json
    try:
        db.collection('personal').document(id_persona).update(datos)
        return jsonify({"mensaje": "Información actualizada exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@personal_bp.route('/personal/<id_persona>', methods=['DELETE'])
def eliminar_personal(id_persona):
    try:
        db.collection('personal').document(id_persona).delete()
        return jsonify({"mensaje": "Personal eliminado exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
