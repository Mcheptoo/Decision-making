sal = int(input("Enter Salary:"))
years = int(input("Enter Years of Service:"))
if (years>10):
    bonus1=(sal*0.1)
    print("Your Bonus is:",bonus1)
elif ((years>=6) and (years<=10)):
    bonus2=(sal*0.08)
    print("Your Bonus is:",bonus2)
elif (years<6):
    bonus3=(sal*0.05)
    print("Your Bonus is:",bonus3)
else:
    print("Try Again")