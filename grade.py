print("Enter Score for 3 Subjects (out of 100)")
sub1 = int(input("Enter Score for Subject 1: "))
sub2 = int(input("Enter Score for Subject 2: "))
sub3 = int(input("Enter Score for Subject 3: "))
total = (sub1+sub2+sub3)
avg = (total/3)
if (avg<=100 and avg>0):
    print("Average Score = ",avg)
if (avg>=70 and avg<=100):
    print("Grade = A")
elif (avg>=60 and avg<=69):
    print("Grade = B")
elif (avg >= 50 and avg <= 59):
    print("Grade = C")
elif (avg >= 40 and avg <= 49):
    print("Grade = D")
elif (avg>0 and avg<=39):
    print("Grade = Fail")
else:
    print("Try Again")