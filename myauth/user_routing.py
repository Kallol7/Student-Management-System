import hashlib

def get_user_bucket(username, maximum= 100):
    bytes = hashlib.sha256(username.encode("utf-8")).digest()
    bytes = bytes[:4] # only first 4 bytes to keep it fast
    hash = int.from_bytes(bytes, 'big')

    return (hash % maximum) + 1

f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=973896962005-89l2t024bf1gv5533pn97n27cubj5jcq.apps.googleusercontent.com&scope=openid%20email&&redirect_uri=http://127.0.0.1:8000/callback&state=foobar&nonce=nonce"
