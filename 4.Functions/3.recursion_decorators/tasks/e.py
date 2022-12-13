_functions_queue = {}
def result_accumulator(method):
    global _functions_queue
    def answer(f):

        def wrapper(*args, **kwargs):
            f_name = f.__name__
            if method == 'accumulate':
                if f_name not in _functions_queue:
                    _functions_queue[f.__name__] = []
                _functions_queue[f.__name__].append(f(*args, **kwargs))
            
            elif method == "drop":
                if f_name not in _functions_queue:
                    res = []
                else:
                    res = _functions_queue[f.__name__]
                return res
        return wrapper
    return answer
   
    

@result_accumulator("accumulate")
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))

