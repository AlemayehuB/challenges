x = input("Enter a string: \n")
vowels = ["a","e", "i", "o", "u"]
add = ""
j = 0
for i in x:
    if i not in vowels:
        add = add + i
        j += 1
    else:
        print (x[j:len(x)] +  add + "ay")
        break
