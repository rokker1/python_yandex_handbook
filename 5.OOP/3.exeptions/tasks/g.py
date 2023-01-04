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

print(name_validation("Ёёёёёёёёё"))