units = int (input("Enter the number of units consumed."))

if( units < 50):
 bill = 2.60*units + 25 
 print("The electricity bill is of Rupees" , bill)
elif ( units >= 50 and units < 100):
 bill = 3.25*units + 35
 print("The bill amount is Rupees" , bill)
elif ( units >= 100 and units < 200):
 bill = 5.26*units + 45
 print("The bill amount is Rupees" , bill)

else: 
 bill = 8.45*units + 75
 print ("The bill is of Rupees" , bill)
 