number = [1,2,3,4,5]
fruits =["apple","banana","mango"]
mixed =["Ong",18,3.87,"FOCS",True]

student_details = ["Bob",22,"Engineering", 3.85, True, ["Python","Java"]]
name, age, major, cgpa, is_active, skills = student_details
print(f"Name: {name}\nAge: {age}")

range_list = list(range(5))
print(range_list)

square_list= [i**2 for i in range(1,6)]
print(square_list)
even_square_list = [i**2 for i in range(1,6) if i % 2 == 0]
print(even_square_list)

numbers = [1,2,3,4,5,6]
first, *middle, last = numbers
print(first)
print(middle)
print(last)

first,second,*remaining = numbers
print(first)
print(second)
print(remaining)

fruits = ["apple","banana","grape"]
fruits = fruits + ["mango"]
fruits.append("mangosteen")
fruits.insert(1,"apple2")
fruits.extend(["durian", "peach"])
fruits.remove("apple")