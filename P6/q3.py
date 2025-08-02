input_list = []

while True:
    user_input =input("Enter an integer or 'Q'/'q' to exit:")

    if user_input.lower() == "q":
            break
    if not user_input.isdigit():
        print("Only integer is allowed!")
        continue
    input_list.append = (int(user_input))

print(input_list[::-1])
