import random

answer_list = []
user_input_list = []
result_list = []
while True:
    try:
        user_input = input("Enter your guess as 1 for a head, 2 for a tail, or 0 to exit:")

        if user_input == 0:
            print("Thank you for playing the game!")
            break
        if user_input not in ["1","2"]:
            raise Exception("Please enter 0, 1, or 2.")
        answer = random.randint(1, 2)
        answer = str(answer)
        answer_list.append(answer)
        user_input_list.append(user_input)
        if answer == user_input:
            print("Correct!")
            result_list.append("Correct")
        else:
            print("Wrong!")
            result_list.append("Wrong")
    except Exception as e:
        print(e)

    count_success= result_list.count("Correct")
    count_fail= result_list.count("Wrong")
    print(f"You have made {count_success} correct guesses and {count_fail} incorrect guess.")
