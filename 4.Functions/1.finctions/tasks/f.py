db = []
def modern_print(string):
    global db
    if not string in db:
        print(string)
    db.append(string)

modern_print()