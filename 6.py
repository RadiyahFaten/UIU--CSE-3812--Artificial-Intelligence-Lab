marks = []

for _ in range(6):
    n = int(input("Enter your marks: "))
    marks.append(n)

for mark in marks:
    print(mark)

print(f"First 3: {marks[0:3]}")
print(f"Last 3: {marks[3:6]}")

total = 0
count = 0

for mark in marks:
    total += mark
    if mark >= 50:
        count += 1


print(f"Total: {total}\nAverage: {total / 6 : .2f}\nPassed Subjects: {count}")

    



    
