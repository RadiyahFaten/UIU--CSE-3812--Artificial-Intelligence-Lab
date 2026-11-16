n = []

for _ in range(8):

    x = int(input("Enter n: "))
    n.append(x);

sum = 0
count = 0

for x in n:
    sum += x

    if x >= 50:
        count += 1

print(f"First three: {n[0:4]}")
print(f"{n[4:8]}")    
print(f"{n[0:8:2]}")
print(f"{n[::-1]}")
print(f"{sum}\n{sum / 8}")