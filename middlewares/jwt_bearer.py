from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request
from utils.jwtmanager import validated_token

class JWTBearer(HTTPBearer):

    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validated_token(auth.credentials)
        if data['email'] != "admin@email.com":
            raise HTTPException(status_code=403, details="credenciales no son validas")