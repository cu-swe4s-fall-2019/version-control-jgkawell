from math_lib import div, add

if __name__ == "__main__":
    a = 3
    b = 2
    c = 0

    div_result = div(a, b)
    print(f"Testing division ({a} / {b}): {div_result}")

    div_result = div(a, c)
    print(f"Testing division ({a} / {c}): {div_result}")

    add_result = add(a, b)
    print(f"Testing addition ({a} + {b}): {add_result}")
