color = input()
match color:
    case 'red' | 'yellow':
        print('stop')
    case 'green':
        print("can go")
    case _:
        print("incorrect value")