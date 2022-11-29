numbers = [int(input()) for i in range(5)]
print(numbers)

matrix = [[int(x) for x in input().split()] for i in range(5)]
print(matrix)

text = "String of characters"
codes = [ord(symbol) for symbol in text]
print(codes)

countries = {"Россия": ["русский"],
             "Беларусь": ["белорусский", "русский"],
             "Бельгия": ["немецкий", "французский", "нидерландский"],
             "Вьетнам": ["вьетнамский"]}
multiple_lang = [country for (country, lang) in countries.items() if len(lang) > 1]
print(multiple_lang)
