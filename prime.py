x = input("Next prime y/n?: \n")
prime = 1
def isPrime(num):
    if num%2 == 0:
        return False

    for i in range(3,num):
        if num % i == 0:
            return False
            break
    return True

while x == 'y':

    if isPrime(prime) != True:
        prime += 1
    else:
        print(str(prime) + " is a prime number")
        prime += 1
    x = input("Next prime y/n?: \n")
