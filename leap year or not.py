#-----------------Question------------------------CHeck if the year is leap or not

year=int(input("Enter Your Year:"))

if (year%400==0) and (year%100==0):
    print(year,"is leap year")
elif (year%4==0) and (year%100!=0):
    print(year,"is a leep year")
else:
    print(year,"is not a leep year")
