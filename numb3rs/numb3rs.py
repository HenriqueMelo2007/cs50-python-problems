import re


def main():
    user_input = input("IPv4 address: ")
    if validate(user_input.strip()):
        print("True")
    else:
        print("False")


def validate(user_input):
    zero_to_max = r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)"
    regex = rf"^{zero_to_max}\.{zero_to_max}\.{zero_to_max}\.{zero_to_max}$"
    return re.search(regex, user_input)


if __name__ == "__main__":
    main()
