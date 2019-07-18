
num_low = 1
num_high = 100
count = 0

print("Think of a number between " + str(num_low) + " and " + str(num_high) + " !") #range can be changed by changing num_low and num_high


while True :  #looping until break
    
    if num_low > num_high : 
        print("User is lying")
        break #Stop looping because User is lying
    
    comp_guess = (num_low + num_high)//2 #starting with the middle of the range
    print("Is your number " + str(comp_guess) + " ?")
    print("")
    clue = input("Is your number higher (<), lower (>) or equal (=) than " + str(comp_guess) + " ? ")
    
    if clue == "=" :
        count += 1
        print("I have guessed it!")
        print("I needed " + str(count) + " steps!")
        break #Stop looping because Computer guessed the right number
    
    elif clue == ">" :
        count += 1
        num_low = comp_guess + 1
    
    elif clue == "<" :
        count += 1
        num_high = comp_guess - 1
    
    else :
        print("Please only use >, < or =") #Tell the user that only >, < or = can be used
    
        
    
    