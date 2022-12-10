def is_palindrome(arg):
    if isinstance(arg, str):
        return arg == arg[::-1]
    elif isinstance(arg, int):
        s = str(arg)
        return s == s[::-1]
    elif isinstance(arg, tuple) or isinstance(arg, list):
        if len(arg) == 0:
            return True
        for i in range(len(arg) // 2):
            if arg[i] != arg[-i - 1]:
                return False
        return True


print(is_palindrome(2332))
print(is_palindrome("afgfa"))
print(is_palindrome((1, 2, 3, 2, 1)))
print(is_palindrome([1, 2, 3, 4, 5]))