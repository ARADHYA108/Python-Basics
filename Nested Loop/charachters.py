word = input("Enter the word ")

character = input("Enter the character you want to search.")

i = 0 

count = 0 

while i < len(word):
    if word [i] == character:
        count += 1 
    i = i + 1  
print("Total no. of times  " , character, "has occured" , count )    
