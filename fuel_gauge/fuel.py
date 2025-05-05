def main():
    x, y = get_user_input()
    percentage = get_percentage(x, y)
    result = get_result(percentage)
    print(result)


def get_user_input():
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


def get_percentage(x, y):
    percentage = x / y * 100
    return round(percentage)


def get_result(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
