from random import randint
import os
import time

again = "y"

def roll():
    list = ["Rolling .","Rolling ..","Rolling ..."]

    for i in range(3):
        for i in list:
            print(i)
            time.sleep(1)
            print ("\033[A                             \033[A")

while again.lower() == "y" :
    print("""
    _______     _____        _____
  /\       \      |    |  |  |
 /()\   ()  \     |    |__|  |___
/    \_______\    |    |  |  |
\    /()     /    |    |  |  |____
 \()/   ()  /       DICE GAME 
  \/_____()/      by ©lonewol7f
""")

    input("Press Enter to Continue ...")
    os.system("cls") #TODO : If you use linux distro, replace 'cls' with 'clear' and edit last line too.

    rnum = randint(1,6) 

    try:
        guess = int(input("Guess the rolled number : "))
        roll()
    
        if rnum == 1:
            print('''    _______     
  /\       \      
 /()\   ()  \     
/    \_______\    
\    /()     /    
 \()/   ()  /            
  \/_____()/''')
    
        elif rnum == 2:
            print('''    _______     
  /\  ()   \      
 /()\   ()  \     
/()()\_______\    
\()()/()     /    
 \()/   ()  /            
  \/_____()/''')
    
        elif rnum == 3:
            print('''    _______     
  /\  ()   \      
 /  \   ()  \     
/ () \_____()\    
\    /()     /    
 \  /   ()  /            
  \/_______/''')
    
        elif rnum == 4:
            print('''    _______     
  /\()   ()\      
 /  \       \     
/ () \()___()\    
\    /()     /    
 \  /   ()  /            
  \/_____()/''')
    
        elif rnum == 5:
            print('''    _______     
  /\()   ()\      
 /()\   ()  \     
/    \()___()\    
\    /       /    
 \()/   ()  /            
  \/_______/''')
    
        else:
            print('''    _______     
  /\()()() \      
 /()\ ()()()\     
/()  \_______\    
\  ()/()     /    
 \()/   ()  /            
  \/_____()/''')

        if guess > 0 & guess <=6:
            if guess == rnum:
                print("\nWOW... You got it (｡◕‿◕｡)")
                print()
                again = input("Do you want play again (y/n) : ")
            elif guess >= 7:
                print("\nYou should enter number between 1 and 6")
                print()
                again = input("Do you want to try again (y/n) : ") 
            else:
                print(f"\nBad luck (ಠ_ಠ) , The number rolled was {rnum}")
                print()
                again = input("Do you want to try again (y/n) : ")     
    
    except:
        print("That is not a Number")
        again = input("Do you want to try again (y/n) : ")

print("\n See you soon (ʘ‿ʘ)╯ ")
time.sleep(3)
os.system("cls")