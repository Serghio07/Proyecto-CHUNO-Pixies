import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Blueprint, request, session, redirect, url_for, flash, render_template

# Configuración de Pyrebase
firebase_config = {
    "apiKey": "AIzaSyCIeYBM8_pmHTB8M5WrKtiYs43STF-Sx2U",
    "authDomain": "chuno-6384b.firebaseapp.com",
    "databaseURL": "https://chuno-6384b-default-rtdb.firebaseio.com",
    "projectId": "chuno-6384b",
    "storageBucket": "chuno-6384b.appspot.com",
    "messagingSenderId": "961285732641",
    "appId": "1:961285732641:web:041aafd7d44b7c0051e660",
    "measurementId": "G-W41SD9B2W8"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Verificar si Firebase Admin ya ha sido inicializado
if not firebase_admin._apps:
    print("Inicializando Firebase Admin SDK...")
    cred = credentials.Certificate('chuno-6384b-firebase-adminsdk-3tk2c-6978abeab8.json')
    firebase_admin.initialize_app(cred)
    print("Firebase Admin SDK inicializado correctamente.")
else:
    print("Firebase Admin SDK ya estaba inicializado.")

# Inicializar Firestore
db = firestore.client()

# Crear el Blueprint
autenticacion_bp = Blueprint('autenticacion_bp', __name__)

# Ruta para manejar el registro
@autenticacion_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']  # Obtener el rol seleccionado

        try:
            # Registrar al usuario en Firebase Authentication
            user = auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']  # ID del usuario creado

            # Guardar el rol del usuario en Firestore
            db.collection('users').document(user_id).set({
                "email": email,
                "role": role
            })
            flash("Registro exitoso, por favor inicia sesión", "success")

            return redirect(url_for('autenticacion_bp.login'))

        except Exception as e:
            flash("Error en el registro: " + str(e), "danger")
            return redirect(url_for('autenticacion_bp.signup'))

    return render_template('signup.html')

# Ruta para manejar el login
@autenticacion_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        try:
            # Iniciar sesión con Pyrebase
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user['localId']
            session['email'] = user['email']

            # Obtener el rol del usuario desde Firestore
            user_ref = db.collection('users').document(user['localId']).get()
            user_data = user_ref.to_dict()

            if user_data is None:
                flash("No se encontró el usuario en la base de datos", "danger")
                return redirect(url_for('autenticacion_bp.login'))

            user_role = user_data.get('role', 'asistente')  # Extraer el rol, por defecto asistente

            # Guardar el rol en la sesión
            session['role'] = user_role

            flash("Inicio de sesión exitoso", "success")

            # Redirigir según el rol
            if user_role == 'asistente':
                return redirect(url_for('asistente_bp.indexO'))
            elif user_role == 'orador':
                return redirect(url_for('orador_bp.indexOR'))
            elif user_role == 'organizador':
                return redirect(url_for('organizador_bp.indexO'))
            else:
                return redirect(url_for('index'))  # En caso de rol inesperado

        except Exception as e:
            flash("Error al iniciar sesión: " + str(e), "danger")
            return redirect(url_for('autenticacion_bp.login'))

    return render_template('inicio_sesion.html')

# Ruta para manejar el cierre de sesión
@autenticacion_bp.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('email', None)
    session.pop('role', None)
    flash("Has cerrado sesión correctamente", "success")
    return redirect(url_for('autenticacion_bp.login'))
