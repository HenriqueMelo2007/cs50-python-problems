import random


def main():
    level: int = get_level()
    random_integer: int = generates_random_integer(level)
    guessing(random_integer)


def get_level() -> int:
    while True:
        try:
            user_input: int = int(input("Level: ").strip())
            if user_input < 1:
                raise ValueError
            return user_input
        except ValueError:
            continue


def generates_random_integer(level) -> int:
    return random.randint(1, level)


def guessing(random_integer) -> None:
    while True:
        try:
            user_input: int = int(input("Guess: ").strip())
            if user_input < 1:
                raise ValueError
            if user_input > random_integer:
                print("Too large!")
            elif user_input < random_integer:
                print("Too small!")
            else:
                print("Just Right!")
                return
        except ValueError:
            continue


if __name__ == "__main__":
    main()
