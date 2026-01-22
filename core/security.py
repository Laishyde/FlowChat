from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str):
    return pwd_context.hash(senha)

def criar_token(dados: dict):
    # token fake só para a aplicação subir
    return "token_fake"
