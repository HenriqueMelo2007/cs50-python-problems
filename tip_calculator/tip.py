def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent / 100
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollar_str):
    return float(dollar_str.replace("$", ""))


def percent_to_float(percent_str):
    return float(percent_str.replace("%", ""))


if __name__ == "__main__":
    main()
