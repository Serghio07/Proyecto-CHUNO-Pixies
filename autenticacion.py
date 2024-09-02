from flask import Blueprint, request, jsonify
import firebase_admin
from firebase_admin import auth, credentials, firestore

# Crear un Blueprint para la autenticación
autenticacion_bp = Blueprint('autenticacion_bp', __name__)

# Configuración de Firebase
try:
    # Verifica si la app de Firebase ya está inicializada
    firebase_admin.get_app()
except ValueError:
    # Si no está inicializada, inicialízala
    cred = credentials.Certificate('chuno-6384b-firebase-adminsdk-3tk2c-6978abeab8.json')
    firebase_admin.initialize_app(cred)

# Conecta a Firestore
db = firestore.client()

@autenticacion_bp.route('/registro', methods=['POST'])
def registro():
    datos = request.json
    email = datos['email']
    contrasena = datos['contrasena']
    rol = datos['rol']  # 'orador', 'asistente', 'organizador'

    try:
        usuario = auth.create_user(
            email=email,
            password=contrasena
        )
        db.collection('usuarios').document(usuario.uid).set({
            'email': email,
            'rol': rol
        })
        return jsonify({"mensaje": "Usuario creado exitosamente"}), 201
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@autenticacion_bp.route('/obtener_rol/<uid>', methods=['GET'])
def obtener_rol(uid):
    try:
        usuario_doc = db.collection('usuarios').document(uid).get()
        if usuario_doc.exists:
            return jsonify(usuario_doc.to_dict()), 200
        else:
            return jsonify({"mensaje": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
