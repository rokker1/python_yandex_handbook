def only_pos(x):
    return x > 0


result = filter(only_pos, [-1, 5, 6, -10, 0])
print(", ".join(str(x) for x in result))

result = filter(str.isalpha, "123ABCdef()")
print("".join(result))

def square(x):
    return x ** 2

result = map(square, range(5))
print(", ".join(str(x) for x in result))


result = map(str.lower, ["abCD", "EFGh", "IJkl"])
print("\n".join(result))


result = map(str.lower, ["SFefWWFvEFCCsdSDVsdvsDVD"])
print("\n".join(result))


result = filter(lambda x: x > 0, [-1, 5, 6, -10, 0])
print(", ".join(str(x) for x in result))


result = map(lambda x: x ** 2, range(5))
print(", ".join(str(x) for x in result))

lines = ["abcd", "ab", "abc", "abcdef"]
print(sorted(lines, key=lambda line: len(line)))