#--------question-------------if a no. is prime or not
num=int(input("enter your number:"))

if  num==1:
    print("it is not a prime  number")
if num>1:
    for i in range(2,num):
        if num%i == 0:
            print("it is not a prime number")
            break
else:
    print("It is a prime number")