hour = int(input("Enter the hours: "))

cost = 0

if hour > 0:

    if hour >= 2:
        cost += 2 * 50
        hour -= 2
    else:
        cost += hour * 50
        hour = 0

    if hour > 3:
        cost += 3 * 30
        hour -= 3
    else:
        cost += hour * 30
        hour = 0

    cost += hour * 20

else: 
    cost = 0

print(f"Total cost: {cost}")               

