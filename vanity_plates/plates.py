def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    length = len(plate)

    if length < 2 or length > 6:
        return False

    numbers_has_started = False

    for i in range(length):

        if not plate[i].isnumeric() and not plate[i].isalpha():
            return False

        if plate[i].isnumeric():
            if i < 2:
                return False
            elif not numbers_has_started and plate[i] == "0":
                return False
            else:
                numbers_has_started = True

        if numbers_has_started and plate[i].isalpha():
            return False

    return True


if __name__ == "__main__":
    main()
