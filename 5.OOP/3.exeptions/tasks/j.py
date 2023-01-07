import hashlib
import binascii
import uu
from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


POSSIBLE_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def password_validation(password, min_length=8, possible_chars=POSSIBLE_CHARS, at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    
    if len(password) < min_length:
        raise MinLengthError
    if any([c not in possible_chars for c in password]):
        raise PossibleCharError
    if not any([at_least_one(c) for c in password]):
        raise NeedCharError

    password_bytes = password.encode('utf-8')
    m = hashlib.sha256()
    m.update(password_bytes)
    return m.hexdigest()


print(password_validation("Hello12345"))
