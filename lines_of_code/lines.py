import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Invalid number of arguments (2 arguments expected)")
    user_file = sys.argv[1]
    if not user_file.endswith(".py"):
        sys.exit("Invalid file extesion (.py required)")
    with open(user_file, "r") as python_file:
        count = 0
        for line in python_file:
            if line.strip() == "" or line.strip().startswith("#"):
                continue
            count = count + 1
        print(count)


if __name__ == "__main__":
    main()
