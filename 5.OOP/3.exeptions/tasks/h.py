class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    
    if any([not (c.isalnum() or c == '_') for c in username]):
        raise BadCharacterError
    
    if username[0].isdigit():
        raise StartsWithDigitError
    
    return username


print(username_validation("u44user"))
