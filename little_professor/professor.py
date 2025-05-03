import random


def main():
    user_level = get_level()
    user_score = 0
    for _ in range(10):
        x = generate_integer(user_level)
        y = generate_integer(user_level)
        correct_sum = x + y
        current_score = check_answer(x, y, correct_sum)
        user_score += current_score
    print(f"SCORE: {user_score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                return level
        except ValueError:
            continue


def generate_integer(user_level):
    a = 10 ** (user_level - 1)
    b = 10**user_level
    return random.randint(a, b - 1)


def check_answer(x, y, correct_sum):
    for _ in range(3):
        try:
            user_answer = int(input(f"{x} + {y} = "))
            if user_answer == correct_sum:
                return 1
            print("EEE")
        except ValueError:
            continue
    print(f"Correct Answer: {correct_sum}")
    return 0


if __name__ == "__main__":
    main()
