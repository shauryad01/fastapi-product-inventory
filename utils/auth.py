import hashlib
from bcrypt import checkpw, hashpw, gensalt

def hash_password(password: str):
    pre_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    hashed = hashpw(pre_hash.encode('utf-8'), gensalt())
    return hashed.decode('utf-8') 

def verify_password(userpassword: str, dbpassword: str):
    pre_hash = hashlib.sha256(userpassword.encode('utf-8')).hexdigest()
    if dbpassword.startswith("b'") or dbpassword.startswith('b"'):
        dbpassword = dbpassword[2:-1]
    return checkpw(pre_hash.encode('utf-8'), dbpassword.encode('utf-8'))

def create_access_token():
    return 123