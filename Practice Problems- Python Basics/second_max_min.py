num = []

for _ in range(5):
    x = int(input("Enter n: "))
    num.append(x)

max = num[0]
second_max = num[0]
min = num[0]
second_min = num[0]

for n in num:
    if n > max:
        second_max = max 
        max = n
    elif (n < max and n > second_max):
        second_max = n    

    if n < min:
        second_min = min
        min = n
    elif (n > min and n < second_min):
        second_min = n

print(f"{second_max}\n{second_min}")