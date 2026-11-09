products = []

n = int(input("Number of Products: "))

for _ in range(n):
    x = int(input("Prices: "))
    products.append(x)

sum = 0
count = 0
for p in products: 
    sum += p

    if p > 500:
        count += 1

total = 0
discount = 0


if sum < 1000:
    total = sum;
    discount = 0

elif sum > 1000 and sum <3000:

    total = sum - (sum * 5) // 100
    discount = (sum * 5) // 100

elif sum > 3000:

    total = sum - (sum * 10) // 100
    discount = (sum * 10) // 100

print(f"Total Bill: {sum}")
print(f"Products above 500: {count}")
print(f"Discount: {discount}")
print(f"final bill: {total}")