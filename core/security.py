import hashlib

from datetime import datetime, timedelta

SECRET_KEY = "4de36fa327d71601985b5bd20b804d679375139f2856d34c57e9eb40caa36048"
ALGORITHM = "HS256"

def hash_senha(senha: str):
    return hashlib.sha256(senha.encode()).hexdigest()

def criar_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=8)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
