#Kavilan Naidoo
#03-10-2014
#numbers of hours of work exercise

hours=int(input("Please enter the amount of hours worked: "))
rate=int(input("Please enter your hourly rate: "))
non_overtime= hours * rate
if hours < 61:
    if hours >40:
        overtime = hours - 40
        overtime_pay = overtime*1.5
        pay= (hours - overtime)*rate
        overall_pay=overtime_pay+pay
        print("Your Overall pay is £{0}".format(overall_pay))
    else:
        
      print("Your overall pay is £{0}".format(non_overtime))

    


        
        

