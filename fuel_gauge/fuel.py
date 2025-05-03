def main():
    x, y = get_fraction()
    percentage = round(x / y * 100)
    result = get_result(percentage)
    print(result)


def get_fraction():
    while True:
        try:
            user_input = input("Fraction: ")
            x, y = user_input.split("/")
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            return x, y
        except (ValueError, ZeroDivisionError):
            continue


def get_result(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
