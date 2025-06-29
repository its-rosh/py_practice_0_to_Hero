#--------------Question--------------print prime no. with in an interval
lower = int(input("enter lower limit:"))
upper= int(input("enter upper limit:"))

for num in range (lower,upper+1):
    if num >1:
        for i in range (2,num):
            if num%i== 0:
                break
        else:
                print("prime number is :",num)