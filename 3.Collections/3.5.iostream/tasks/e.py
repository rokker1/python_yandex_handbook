from sys import stdin

def check_palindrome(text):
    return text.lower() == text.lower()[::-1]

palidromes = set()
for line in stdin:
    for word in line.rstrip("\n").split():
        if check_palindrome(word):
            palidromes.add(word)

for word in sorted(palidromes):
    print(word)