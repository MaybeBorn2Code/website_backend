# Django
from django.conf import settings

# JWT
import jwt

# Python
from datetime import datetime, timedelta


def create_jwt_token(user_id):
    iat = datetime.utcnow()
    payload = {
        'user_id': user_id,
        'exp': iat + timedelta(days=1),
        'iat': iat,
    }
    token = jwt.encode(
        payload=payload, 
        key=settings.SECRET_KEY, 
        algorithm='HS256'
    )
    return token

