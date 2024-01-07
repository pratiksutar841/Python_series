# take the percentage of student and print there grade according to there marking system

marks=int(input("Enter the student marks : "))

if marks > 80:
          print("Very Good")
elif marks > 60:
        print("Good")
elif marks > 50:
        print("Average")
else:
        print("Fail")



eng_marks=int(input("Enter the English marks : "))
Sci_marks=int(input("Enter the Science marks : "))
if eng_marks > 80 and Sci_marks >80:
       print("A grade")
elif eng_marks > 80 or Sci_marks >80:
       print("B grade")
else:
       print("c grade")
