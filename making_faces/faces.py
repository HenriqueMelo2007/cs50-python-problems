def main():
    replacements = {":)": "🙂", ":(": "🙁"}
    user_input = input("Type your text: ")

    for key, value in replacements.items():
        user_input = user_input.replace(key, value)

    print(user_input)

if __name__ == "__main__":
    main()
