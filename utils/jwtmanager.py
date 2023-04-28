from jwt import encode, decode

def create_tocken(data: dict):
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token

def validated_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithm=['HS256'])
    return data