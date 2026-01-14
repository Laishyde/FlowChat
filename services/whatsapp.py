import requests

TOKEN = "SEU_TOKEN_META"
PHONE_ID = "SEU_PHONE_ID"

def enviar_mensagem(telefone, texto):
    url = f"https://graph.facebook.com/v19.0/{PHONE_ID}/messages"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": telefone,
        "type": "text",
        "text": {"body": texto}
    }

    requests.post(url, headers=headers, json=payload)
