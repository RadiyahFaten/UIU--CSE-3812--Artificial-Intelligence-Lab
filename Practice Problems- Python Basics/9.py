num = []

for _ in range(5):
    n = int(input("Enter num: "))
    num.append(n)

max = num[0]
min = num[0]

for n in num:
    if n >= max:
        max = n
    elif n < min:
        min = n

print(f"Max: {max}\nMin: {min}\nDifference: {max - min}")
        