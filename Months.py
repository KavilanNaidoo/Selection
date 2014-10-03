#Kavilan Naidoo
#selection improvement exercise
#26-09-2014

month = int(input("Please enter a month as a number between 1-12: "))

if month == 12:
    print("The month you entered is December")
elif month ==11 :
    print("The month you entered is November")
elif month == 10:
    print("The month you entered is October")
elif month == 9:
    print("The month you entered is September")
elif month ==8:
    print("The month you entered is August")
elif month == 7:
    print("The month you entered is July")
elif month == 6:
    print("The month you entered is June")
elif month ==5 :
    print("The month you entered is May")
elif month == 4:
    print("The month you entered is April")
elif month == 3:
    print("The month you entered is March ")
elif month == 2:
    print("The month you entered is February")
elif month == 1:
    print("The month you entered is January")
else:
    print("You have entered an invalid number - try again")

year = int (input("Please enter the year: "))
if year % 4 ==0:
    print("It's a leap year")
else:
    print("It's not a leap year")
    
