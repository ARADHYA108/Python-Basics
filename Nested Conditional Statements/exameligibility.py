cause = input("Do you have any medical cause? (Y/N)")

if ( cause == "Y"):
    print("The student is eligible to take the exam.")
elif cause == "N":
    attendance = float (input("Enter your attendance"))  
    if (attendance > 75 ):
     print("The student is allowed to give the exam.")
    else:
     print("The student is not allowed to give the exam.")
else:
    print("Enter valid input (Y/N)")      