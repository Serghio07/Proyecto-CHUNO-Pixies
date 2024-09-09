from flask import Blueprint, request, jsonify
import sendgrid
from sendgrid.helpers.mail import Mail
from twilio.rest import Client

notificaciones_bp = Blueprint('notificaciones_bp', __name__)

# Configurar SendGrid
sg = sendgrid.SendGridAPIClient(api_key='TU_API_KEY_DE_SENDGRID')

# Configurar Twilio
twilio_client = Client("TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN")

@notificaciones_bp.route('/enviar_correo', methods=['POST'])
def enviar_correo():
    datos = request.json
    email = datos['email']
    asunto = datos['asunto']
    contenido = datos['contenido']

    try:
        mensaje = Mail(
            from_email='tu-email@dominio.com',
            to_emails=email,
            subject=asunto,
            html_content=contenido
        )
        sg.send(mensaje)
        return jsonify({"mensaje": "Correo enviado exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400

@notificaciones_bp.route('/enviar_sms', methods=['POST'])
def enviar_sms():
    datos = request.json
    para = datos['para']
    cuerpo_mensaje = datos['mensaje']

    try:
        mensaje = twilio_client.messages.create(
            body=cuerpo_mensaje,
            from_='+1234567890',  # Número de Twilio
            to=para
        )
        return jsonify({"mensaje": "SMS enviado exitosamente"}), 200
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
