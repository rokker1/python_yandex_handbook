def transliterate(text):
    dictionary = {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Е": "E",
        "Ё": "E",
        "Ж": "ZH",
        "З": "Z",
        "И": "I",
        "Й": "I",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "KH",
        "Ц": "TC",
        "Ч": "CH",
        "Ш": "SH",
        "Щ": "SHCH",
        "Ы": "Y",
        "Э": "E",
        "Ю": "IU",
        "Я": "IA",
        "Ъ": "",
        "Ь": ""
    }
    output_text = ""
    for letter in text:
        if letter.upper() in dictionary:
            if letter.isupper():
                output_text += dictionary[letter].capitalize()
            else:
                output_text += dictionary[letter.upper()].lower()
        else:
            output_text += letter
    return output_text


workdir = "f:/source/python_yandex_handbook/3.Collections/3.5.iostream/tasks/"
with open(workdir + "cyrillic.txt", "r", encoding="UTF-8") as input_file, \
    open(workdir + "transliteration.txt", "w", encoding="UTF-8") as output_file:
    for line in input_file:
        print(transliterate(line.rstrip("\n")), file=output_file)
