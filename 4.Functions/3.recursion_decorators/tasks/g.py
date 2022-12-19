def same_type(f):
    def type_checker(*args):
        for i in range(len(args) - 1):
            if not isinstance(args[i], type(args[i + 1])):
                print("Обнаружены различные типы данных")
                return
        return f(*args)
    return type_checker


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')


@same_type
def combine_text(*words):
    return ' '.join(words)


print(combine_text('Hello,', 'world!') or 'Fail')
print(combine_text(2, '+', 2, '=', 4) or 'Fail')
print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')
