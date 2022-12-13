def shout(word="yes"):
    return word.capitalize() + '!'

print(shout())
# выведет: 'Да!'

scream = shout
print(scream())


del shout
scream()


def talk():
    def whisper(word='yes'):
        return word.lower()+"..."
    print(whisper())

talk()

def get_talk(type="shout"):
    def shout(word="yes"):
        return word.capitalize() + '!'

    def whisper(word='yes'):
        return word.lower()+"..."

    # Затем возвращаем необходимую
    if type == "shout":
        # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
        # а вернуть объект функции
        return shout
    else:
        return whisper


talk = get_talk()
print(talk)


def do_something(func):
    print( )