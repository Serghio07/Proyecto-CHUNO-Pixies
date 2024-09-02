import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, request, jsonify

# Configuración de Firebase
cred = credentials.Certificate('Backend/Clave.json')
firebase_admin.initialize_app(cred)

# Inicializa Firestore DB
db = firestore.client()

# Configuración de Flask
app = Flask(__name__)

# Ruta principal que obtiene datos de Firebase
@app.route('/')
def home():
    docs = db.collection('tu-coleccion').get()
    datos = [doc.to_dict() for doc in docs]
    return render_template('index.html', datos=datos)

# Ruta para agregar datos
@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    db.collection('tu-coleccion').add(data)
    return jsonify({"message": "Data added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
