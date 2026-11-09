n = int(input("Enter a number: "))
count = 0;
sum = 0;

temp = n;

while temp > 0:

    sum += temp % 10
    count += 1
    temp = temp // 10;
    
print(f"Sum of Digits: {sum}")
print(f"Total Digits: {count}")
print(f"Last digit: {n % 10}")
    
    
    






