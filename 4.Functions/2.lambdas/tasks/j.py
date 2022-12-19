import itertools

def secret_replace(word, **kwargs):
    res = ""
    generators = {k: (s for s in itertools.cycle(v)) for k, v in kwargs.items()}
    for c in word:
        if c in kwargs:
            res += next(generators[c])
        else:
            res += c
    return res

result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
print(result)