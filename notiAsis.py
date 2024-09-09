from flask import Blueprint, request, jsonify
from firebase_admin import firestore

notificaciones_bp = Blueprint('notificaciones_bp', __name__)
db = firestore.client()

@notificaciones_bp.route('/notificaciones', methods=['POST'])
def enviar_notificacion():
    datos = request.json
    try:
        db.collection('notificaciones').add(datos)
        return jsonify({"mensaje": "Notificación enviada exitosamente"}), 201
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@notificaciones_bp.route('/notificaciones', methods=['GET'])
def obtener_notificaciones():
    try:
        notificaciones = db.collection('notificaciones').get()
        lista_notificaciones = [noti.to_dict() for noti in notificaciones]
        return jsonify(lista_notificaciones), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
