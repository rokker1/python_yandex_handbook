string = 'мама мыла раму'
print(sorted(string.split(), key=lambda line: (len(line), line.lower())))