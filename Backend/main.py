from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Configuración de la base de datos
DATABASE = {
    'host': 'localhost',
    'database': 'nombre_de_tu_base_de_datos',
    'user': 'tu_usuario',
    'password': 'tu_contraseña'
}

def get_db_connection():
    conn = psycopg2.connect(
        host=DATABASE['host'],
        database=DATABASE['database'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        cursor_factory=RealDictCursor
    )
    return conn

@app.route('/')
def home():
    return "Bienvenido a CHUNO"

@app.route('/about')
def about():
    # Ejemplo de una consulta a la base de datos
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM about')
    about_info = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(about_info)

@app.route('/services')
def services():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM services')
    services_info = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(services_info)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)',
        (name, email, message)
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        'status': 'success',
        'message': f'Gracias, {name}. Hemos recibido tu mensaje.'
    })

if __name__ == '__main__':
    app.run(debug=True)
