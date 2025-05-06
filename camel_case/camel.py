def main():
    camel_case_input = input("Camel case variables: ")
    camel_case_list = camel_case_input.split(" ")
    for camel_case_variable in camel_case_list:
        snake_case_variable = camel_case_to_snake_case(camel_case_variable)
        print(snake_case_variable, end=" ")


def camel_case_to_snake_case(camel_case_variable):
    snake_case = ""
    for c in camel_case_variable:
        if c.isupper():
            snake_case += "_" + c.lower()
        else:
            snake_case += c
    if snake_case.startswith("_"):
        snake_case = snake_case[1:]
    return snake_case


if __name__ == "__main__":
    main()
