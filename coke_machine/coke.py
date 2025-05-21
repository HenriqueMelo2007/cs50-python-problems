def main():
    amount_due = 50
    change_owed = 0
    valid_values = [25, 10, 5]
    while True:
        user_input = int(input("Coin: "))
        if user_input not in valid_values:
            print(f"Amount due: {amount_due - change_owed}")
            continue
        change_owed += user_input
        if change_owed >= amount_due:
            print(f"Change owed: {change_owed - amount_due}")
            break
        print(f"Amount due: {amount_due - change_owed}")


if __name__ == "__main__":
    main()
