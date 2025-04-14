def main():
  user_input = input("Greeting: ").lower().strip()
  if "hello" in user_input:
    print("$0")
  elif user_input[0] == "h":
    print("$20")
  else:
    print("$100")
      

if __name__ == "__main__":
    main()