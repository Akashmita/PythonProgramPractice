#less than 2 not prime
#rest numbers check

lower=int(input("Enter lower range starting number: "))
upper=int(input("Enter upper range ending number: "))

for num in range(lower, upper+1): #range to check if any number is prime or not
    if num <= 1:
        print(f"{num} is not a prime number:")
    elif num > 1:
        for i in range(2, num):
            #will check first num in range with 2 to num-1, iterate till it gets "not a prime number"
            if (num % i) == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
            #if we write it inside for loop it will not allow to iterate after checking with 2











