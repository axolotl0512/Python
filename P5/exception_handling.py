def divide_number(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Invalid Input")
        return None

    else:
        print(f"The result of {x}/{y} is {result}")
        return result
    finally:
        print("Operation is a success")

divide_number(3,0)
divide_number('a','b')
divide_number(8,2)

def validate_age(age):
    try:
        if age < 0:
            raise ValueError("Invalid Age")
        elif age < 18:
            print("User is lesser than 18")
        else:
            print("User is an adult")
    except ValueError as e:
        print(f"Errpr occured: {e}")

validate_age(-5)
validate_age(13)
validate_age(20)
