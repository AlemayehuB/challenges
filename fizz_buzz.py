x = input("Enter a number: \n")

def fizz_buzz(n):
    if (n%3 == 0 and n%5 == 0):
        print("FizzBuzz")
        return True
    elif (n%3 == 0):
        print("Fizz")
        return True
    elif (n%5 == 0):
        print("Buzz")
        return True

for i in range(1,int(x)+1):
    if fizz_buzz(i) != True:
        print(i)
