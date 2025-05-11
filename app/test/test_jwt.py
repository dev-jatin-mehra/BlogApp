import jwt
import time
from jwt.exceptions import ExpiredSignatureError,InvalidTokenError

import secrets
secret_key = secrets.token_hex(256)

payload = {"user_id": 1, "exp": int(time.time()) + 5}
token = jwt.encode(payload, secret_key, algorithm="HS256")
print("Generated Token:", token)
print("\n")
print(secret_key)


# Wait for the token to expire
# print("Waiting for the token to expire...")
# time.sleep(6)

# Try to decode and validate the token
try:
    decoded_data = jwt.decode(token, secret_key, algorithms=["HS256"])['user_id']
    print("Decoded Data:", decoded_data)
except ExpiredSignatureError:
    print("Error: Token has expired!")
except InvalidTokenError:
    print("Error: Invalid token!")