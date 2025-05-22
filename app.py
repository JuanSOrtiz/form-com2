from flask import Flask, request, render_template
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./credenciales.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    correo = request.form['correo']
    mensaje = request.form['mensaje']

    doc_ref = db.collection('mensajes').add({
        'nombre': nombre,
        'correo': correo,
        'mensaje': mensaje
    })

    return "¡Formulario enviado y guardado en Firebase!"

if __name__ == '__main__':
    app.run(debug=True)
