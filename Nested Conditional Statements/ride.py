ride = input("Please enter your ride preference (Bike/Car)")
 
if(ride == "Bike"):
    model = input("Activa/Honda")
    if model == "Activa":
        print("Enjoy scooty ride")
    else:  
        print("Enjoy bike ride")  
elif ride == "Car":   
     model = input("Lexus/Hector") 
     if model == "Lexus":
      print("Enjoy your ride with Lexus.")
     else:
         print("Enjoy your ride with Hector") 

else:
    print("Enter valid preference (Bike/Car)")         