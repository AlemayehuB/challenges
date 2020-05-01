x = input("Enter a string: \n")
vowels = ["a","e","i","o","u"]
count = 0
for i in x:
    if i in vowels:
            count += 1

print("There are " + str(count) + " vowels" + " in " + x )
