from flask import Blueprint, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

# Crear un Blueprint para manejar las rutas de contacto
contacto_bp = Blueprint('contacto_bp', __name__)

# Configuración de Firebase (esto debería apuntar a tu archivo de credenciales)
cred = credentials.Certificate('chuno-6384b-firebase-adminsdk-3tk2c-6978abeab8.json')
firebase_admin.initialize_app(cred)

# Inicializar Firestore DB
db = firestore.client()

@contacto_bp.route('/contacto', methods=['POST'])
def contacto():
    # Obtener datos del formulario
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    mensaje = request.form.get('mensaje')

    # Crear un documento en la colección "dudas"
    try:
        db.collection('dudas').add({
            'nombre': nombre,
            'email': email,
            'mensaje': mensaje
        })
        return jsonify({"mensaje": "Gracias por contactarnos. Tu mensaje ha sido recibido."}), 200
    except Exception as e:
        return jsonify({"mensaje": f"Error al guardar en Firestore: {str(e)}"}), 500
