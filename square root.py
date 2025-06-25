# Question ----------- program to find square root of 2 numbers 
#sol using exponentiation(giving power)
num=64
num1 =int(input("Enter A Number Here:"))
sr= num1**(1/2)
print("The Square root of tha number is :",sr)

#using math module
import math
num=int(input("Enter a number here:"))
sr = math.sqrt(num)
print("Square root of the number is",sr)