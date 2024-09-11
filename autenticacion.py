from flask import Blueprint, request, redirect, url_for, flash, render_template, session, jsonify
import firebase_admin
from firebase_admin import auth, credentials

# Crear el Blueprint para autenticación
autenticacion_bp = Blueprint('autenticacion_bp', __name__)


# Ruta para manejar el registro de nuevos usuarios
@autenticacion_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        role = request.form['role']

        try:
            # Crear el usuario en Firebase Authentication
            user = auth.create_user(
                email=email,
                password=password,
                display_name=username
            )
            # Aquí puedes guardar el rol del usuario en Firestore u otra base de datos, si es necesario
            # db.collection('roles').document(user.uid).set({'role': role})
            flash("Usuario registrado exitosamente", "success")
            return redirect(url_for('autenticacion_bp.login'))  # Redirigir al formulario de login
        except Exception as e:
            flash(f"Error al registrar: {str(e)}", "error")
            return render_template('signup.html')
    return render_template('signup.html')

# Ruta para manejar el inicio de sesión
@autenticacion_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.json
        try:
            # Guardar los datos del usuario en la sesión
            session['user_id'] = data['uid']
            session['user'] = {
                'email': data['email'],
                'name': data['displayName'],
                'role': 'asistente'  # Aquí puedes agregar la lógica para obtener el rol desde Firebase o Firestore
            }
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"success": False, "message": str(e)}), 400

# Ruta para manejar el cierre de sesión
@autenticacion_bp.route('/logout')
def logout():
    # Eliminar los datos de la sesión
    session.pop('user_id', None)
    session.pop('user', None)
    flash("Has cerrado sesión correctamente", "success")
    return redirect(url_for('autenticacion_bp.login'))
