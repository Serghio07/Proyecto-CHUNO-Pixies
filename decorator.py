from functools import wraps
from flask import session, redirect, url_for, flash

# Decorador para verificar si el usuario está autenticado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Necesitas iniciar sesión para acceder a esta página", "warning")
            return redirect(url_for('autenticacion_bp.login'))
        return f(*args, **kwargs)
    return decorated_function
