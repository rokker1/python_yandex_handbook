import numpy as np
import pandas as pd


def length_stats(text):
    words = [w for w in text.lower().split()]
    prepared_words = []
    for w in words:
        word = "".join([c for c in w if c.isalpha()])
        if word:
            prepared_words.append(word)
    return pd.Series({word: len(word) for word in sorted(prepared_words)}, dtype="int64")

print(length_stats("44 55 666"))
print(length_stats('Мама мыла раму'))
print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))
print(length_stats('Ёлка, елка, ёлка ЕЛКА'))
