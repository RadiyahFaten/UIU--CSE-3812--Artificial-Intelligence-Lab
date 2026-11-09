n = int(input("Enter a number: "))

even_sum = 0
even_count = 0
odd_sum= 0
odd_count = 0


for x in range(1, n):

    if x % 2 == 0:
        even_sum += x
        even_count += 1
    else:
        odd_sum += x
        odd_count += 1;

print(f"Even Sum: {even_sum}")
print(f"Even Count: {even_count}")
print(f"Odd Sum: {odd_sum}")
print(f"Odd Count: {odd_count}")
