_functions_queue = {}
def result_accumulator(f):
    global _functions_queue
    def wrapper(*args, method = "accumulate", **kwargs):
        f_name = f.__name__
        if method == 'accumulate':
            if f_name not in _functions_queue:
                _functions_queue[f.__name__] = []
            _functions_queue[f.__name__].append(f(*args, **kwargs))
        
        elif method == "drop":
            if f_name not in _functions_queue:
                res = []
                res.append(f(*args, **kwargs))
            else:
                res = _functions_queue[f.__name__][:]
                res.append(f(*args, **kwargs))
                _functions_queue[f.__name__].clear()
            return res
    
    return wrapper

   
    

@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))

