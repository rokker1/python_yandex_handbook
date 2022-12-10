def can_eat(x, y):
    dx = y[0] - x[0]
    dy = y[1] - x[1]
    if abs(dx) + abs(dy) == 3:
        return True
    else:
        return False