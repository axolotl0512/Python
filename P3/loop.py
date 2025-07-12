range(5)
for i in range(5):
    print(i)

names = ["Alice","BOBBY","Charley"]
for i, name in enumerate(names):
    print(f"Index: {i}, Name: {name}")

for i in range(0,10,2):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    print(count)
    count += 1
    if(count>5):
        break