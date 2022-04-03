import time
ussy = "ussy" #declaring variables
word = " "
cont = "Y"

while cont == "Y":   
    word = input(str("Enter your word here: ")) #user input
    print("Calculating")
    time.sleep(2)
    print("Calculating...")
    time.sleep(2)
    merge = word[0:5]
    full = merge + ussy
    print(full)
    cont = input(str("Do you want to ussy another wordussy? (Y/N) "))
    cont = cont.upper()
    print("")
    
    
    
