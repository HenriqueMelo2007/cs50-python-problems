def main():
    while True:
        try:
            user_input = input("Fraction: ")
            x, y = user_input.split('/')
            x = int(x)
            y = int(y)
            if y == 0 or x > y:
                raise ValueError
            percentage = round(x / y * 100)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            continue

if __name__ == "__main__":
    main()