import jwt   # PyJWT 
import uuid

payload = {
    'access_key': '''-----BEGIN ACCESS KEY-----
3EhTwzfqMPbtQQpXryqLjWiSeufYyRXKUAWeUiBS
-----END ACCESS KEY-----''',
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, '''-----BEGIN SECRET KEY-----
ygxjeIZ6eWNerlNutkDje1xPhbIxK00jxqmyE53Q
-----END SECRET KEY-----''')
authorization_token = 'Bearer {}'.format(jwt_token)




# access key

# 3EhTwzfqMPbtQQpXryqLjWiSeufYyRXKUAWeUiBS

# secret key

# ygxjeIZ6eWNerlNutkDje1xPhbIxK00jxqmyE53Q


