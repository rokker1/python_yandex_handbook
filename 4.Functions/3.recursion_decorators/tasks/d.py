def answer(f):
    def inner_function(*args):
        return f"Результат функции: {f(*args)}"
    return inner_function

@answer
def a_plus_b(a, b):
    return a + b

print(a_plus_b(3, 4))

@answer
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))

print(get_letters('Декораторы это круто =)'))