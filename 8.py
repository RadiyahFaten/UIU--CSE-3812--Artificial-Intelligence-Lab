num = []

for _ in range(8):
    x = int(input("Enter num: "))
    num.append(x)

print(f"First 4: {num[0:4]}\nLast 4: {num[4:8]}\nAlternative:{num[0:8:2]}\nReversed: {num[::-1]}")
