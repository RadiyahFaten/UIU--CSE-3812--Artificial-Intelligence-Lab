str = input("Enter a string: ")

count_v = 0
count_c = 0


if str.isalpha():
    for s in str:
        if s != 'a' and s != 'e' and s != 'i' and s !='o' and s != 'u':
            count_c += 1

        else:
            count_v += 1

print(f"Vowels: {count_v}\nConsonants: {count_c}")