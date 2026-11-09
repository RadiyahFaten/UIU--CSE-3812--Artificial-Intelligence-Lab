num = []

for _ in range(8):
    x = int(input("Enter a num: "))
    num.append(x)

count_pos = 0
count_neg = 0
count_zero = 0

for n in num:
    if n > 0:
        count_pos += 1
    elif n < 0:
        count_neg += 1
    else:
        count_zero +=1

print(f"Positive: {count_pos}\nNegative: {count_neg}\nZero: {count_zero}")