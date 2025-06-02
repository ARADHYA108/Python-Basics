amt =  int (input("Enter the amount"))
note1 = amt//100
note2 = amt%100//50
note3 = ((amt%100)%50)//10
print("Count of note1 is" , note1)
print("Count of note2 is" , note2)
print("Count of note3 is" , note3)