"""-----------Quersion----------------How get factorial of any num
Factoiral ex:- 5 =5!
1st using for loop"""
num=int(input("Enter your number:"))
fact=1

if num<0:
    print("factorial of 0 does not exist")
if num ==0:
    print("factroial of 0 is",1)
if num>0:
    for i in range(1,num+1):
        fact=fact*i
    print("the factorial of number is",fact)

#using recursion------- recusion= function will call it self again and again

def fact(a):
    if a==0:
        return 1
    else:
        return ((a)*fact(a-1))
    
num=int(input("Enter your number:"))

result=fact(num)
print("The factorial of the given number is",result)