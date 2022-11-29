text = 'Мама мыла раму!'
my_dict = {
    c.lower() : text.lower().count(c) for c in set(text.lower()) if c.isalpha()
}
print(my_dict)