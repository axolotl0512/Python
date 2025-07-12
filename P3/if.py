print(int(True))
print(int(False))

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(3.14))

print(1>2)

if 1>2:
    print("One is more than Two")

else : 
    print("One is lesser than Two")

def is_weak_password(password):
    if len(password) < 8:
        return True
    else : 
        return False
    
def better_is_weak_password(password):
    return len(password) < 8

print(is_weak_password("123456"))
print(is_weak_password("12345678"))

password ="123456"
is_weak_password = "T" if len(password) < 8 else "F"

def is_strong_password(password):
    if len(password) < 8:
        return False
    elif any(p.isdigit() for p in password) and any(p.isalpha() for p in password):
        return True
    else:
        return False
print(is_strong_password("aA1234567"))

day = "Wednesday"
match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _: #wildcard
        print("Invalid")

age = 19
match age:
    case _ if age < 13:
        print("G or PG Only")
    case _ if age < 17:
        print("Pg-13 is allowed")
    case _ if age < 18:
        print("R allowed with parents")
    case _:
        print("do whatever you want bro :/")

numbers = [0,1,2,3,4,5]
print(any(n%2 != 0 for n in numbers))

#git config --global user.name "Bryan"
#git config --global user.email "bryanskh-wm24@student.tarc.edu.my"
















     