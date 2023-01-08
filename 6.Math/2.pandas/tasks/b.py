import pandas as pd


def length_stats(text):
    words = set(text.lower().split())
    prepared_words = []
    for w in words:
        word = "".join([c for c in w if c.isalpha()])
        if word:
            prepared_words.append(word)
    odd = dict()
    even = dict()
    for prepared_word in sorted(prepared_words):
        leng = len(prepared_word)
        if leng % 2 == 1:
            odd[prepared_word] = leng
        else:
            even[prepared_word] = leng
    return pd.Series(odd, dtype="int64"), pd.Series(even, dtype="int64")

odd, even = length_stats('Мама мыла раму')
print(odd)
print(even)

odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
print(odd)
print(even)
