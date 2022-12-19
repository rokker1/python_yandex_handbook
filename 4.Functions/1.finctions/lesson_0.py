def inc():
    global x
    x += 1
    print(f"Call count: {x}")

x = 0
inc()
inc()
inc()