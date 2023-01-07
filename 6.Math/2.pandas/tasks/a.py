import numpy as np
import pandas as pd


def length_stats(text):
    words = [w for w in text.lower().split()]
    prepared_words = []
    for w in words:
        prepared_words.append("".join([c for c in w if c.isalpha()]))
    return pd.Series({word: len(word) for word in sorted(prepared_words)})


print(length_stats('Мама мыла раму'))
print(length_stats('Лес, опу3шка, 1странный 2домик. Лес, 32опушк23а и зве453рушка.'))

