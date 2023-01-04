class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    nname = name.replace("ё", "е")
    nname = nname.replace("Ё", "Е")
    if not isinstance(nname, str):
        raise TypeError
    if not all([ord("А") <= ord(c) <= ord("я") for c in nname]):
        raise CyrillicError
    if len(nname) > 1:
        if any((ord(c) < ord("а") for c in nname[1:])):
            raise CapitalError
    if len(nname) > 0:
        if ord(nname[0]) > ord("Я"):
            raise CapitalError
    else:
        raise CapitalError
    return name


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


def user_validation(*args, last_name=None, first_name=None, username=None, **kwargs):
    if (not (last_name and first_name and username)) or args or kwargs:
        raise KeyError
    for kwarg in [last_name, first_name, username]:
        if not isinstance(kwarg, str):
            raise TypeError
    for name in [last_name, first_name]:
        name_validation(name)
    username_validation(username)
    return {"last_name": last_name, "first_name": first_name, "username": username}

print(user_validation(last_name="Иванов", first_name="Иван", username='45'))

