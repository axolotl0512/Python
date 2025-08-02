

while True:
    try:
        user_input =input("Enter a score or 'Q'/'q' to exit:")
        if user_input.lower() == "q":
            break
        if user_input.isdigit():
            raise Exception("Only number is allowed!")
        user_input = float(user_input)
        if user_input < 0 or user_input > 100:
            raise Exception("Only 0 ≤ number ≤ 100 inclusive are allowed!")
        
        if user_input >= 90:
            grade = "A"
        elif user_input >= 80:
            grade = "B"
        else:
            grade = "C"
        print(f"You got an {grade} for the test")
    except Exception as e:
        print(e)
