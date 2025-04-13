import hashlib

def get_user_bucket(username, maximum= 100):
    bytes = hashlib.sha256(username.encode("utf-8")).digest()
    bytes = bytes[:4] # only first 4 bytes to keep it fast
    hash = int.from_bytes(bytes, 'big')

    return (hash % maximum) + 1
