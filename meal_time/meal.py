def main():
    user_input: str = input("What time is it? ")
    converted_time: float = convert(user_input)
    output: str = check(converted_time)
    if output:
        print(output + " time")


def convert(user_input) -> float:
    hour, minute = user_input.split(":")
    return float(hour) + (float(minute) / 60)


def check(converted_time) -> str:
    meal_list = [
        {"start": 7, "end": 8, "meal": "Breakfast"},
        {"start": 12, "end": 13, "meal": "Lunch"},
        {"start": 18, "end": 19, "meal": "Dinner"},
    ]

    for meal in meal_list:
        if converted_time >= meal["start"] and converted_time <= meal["end"]:
            return meal["meal"]

    return ""


if __name__ == "__main__":
    main()
