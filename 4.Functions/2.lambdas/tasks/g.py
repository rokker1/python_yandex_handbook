db1 = []
db2 = []

def enter_results(*args):
    global db1
    global db2
    for i in range(0, len(args), 2):
        db1.append(args[i])
        db2.append(args[i + 1])
    

def get_sum(*args):
    global db1, db2
    return (sum(db1), sum(db2))


def get_average(*args):
    global db1, db2
    return (sum(db1) / len(db1), sum(db2) / len(db2))