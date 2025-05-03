def main():
    x, y = get_fraction()
    percentage = round(x / y * 100)
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


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


if __name__ == "__main__":
    main()
