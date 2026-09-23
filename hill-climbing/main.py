def neighbours(x, step):
    return x - step, x + step


def f(x):
    return -pow(x, 2) + 5


def simple_hill_climbing(start):
    x = start
    step = 0.1
    print(f"start: x={x:.4f}, f(x)={f(x):.4f}")
    while True:
        n1, n2 = neighbours(x, step)
        if f(n1) > f(x):
            x = n1
        elif f(n2) > f(x):
            x = n2
        else:
            return x
        print(f"step:  x={x:.4f}, f(x)={f(x):.4f}")


if __name__ == "__main__":
    print("Peak found at x =",int(simple_hill_climbing(3)))
