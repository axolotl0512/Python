
unique_number = {1,2,3,4,5}
number_list = {1,2,3,4,5,5}
unique_number_set = set(number_list)

set_a = {1,2,3}
set_b = {3,4,5}

intersection = set_a & set_b
union = set_a
difference = set_a - set_b
symmetric_difference = set_a ^ set_b

number_set = {1,2,3,4,5}
input = 3
print(input in number_set)

student_grades = {"Alice" : 85,"Bob": 65,"Charles": 90}
input = "Alice"
print(student_grades[input])

student_grades["David"] = 60
student_grades["Alice"] = 75

string_list = ["a","b","c","d"]
formatted_string_list = [s+"a" for s in string_list]
print(formatted_string_list)

student_grades = {"Alice" : 85,"Bob": 65,"Charles": 90}
upper_student_grades = { name.upper():grade for name, grade in student_grades.items()}
print(upper_student_grades)

student_grades = {"Alice" : 85,"Bob": 65,"Charles": 90}
modified_student_grade = {name.lower(): grade+5 for name, grade in student_grades.items()}
print(modified_student_grade)

name = ["Alice","Bob","Charles"]
age = [25,18,30]

combine = dict(zip(name,age))
print(f"{combine}")


