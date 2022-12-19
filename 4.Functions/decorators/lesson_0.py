def identify(f):
    return f


@identify
def foo():
    return 'bar'


#is equal to:
def foo():
    return 'bar'
foo = identify(foo)