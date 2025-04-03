"""
20/2/25
Sarvesh Thiagarajan
This program handles 3 amusement park attractions and whether 
a user can be allowed to go on a ride, how long they have to
wait and if they need less or more people for a ride.

-------------------------------------------------------------

Variable list and scopes.

1. choice - This variable handles the user's input for which
ride they would like to go on, it can only be used in the 
'question()' function.

2. hours - Handles asking the user for how many stem hours
they have. Exists in the 'question()' function and can only be
used there.

3. option - Handles the functions return value of whether a user
fulfills the nstem hours quota or not. Exists within the question()
function and can only be used there.

4. life - Handles the user's input to whether the user has a life
or not. Exists within the question() function and can only be used 
there.

5. ppl_count - Handles the user's input to how many people are
going to be with them for the ACDEC teams Exists within the question()
function and can only be used there.

6. y - This variable is created inside the stem_hours_ride() function
parameter and can only be used within that function. It handles checking
the user's stem hours.

7. x - Handles calculating how many teams can be created for the acdec
team. Can only be used within the acdec_ride() function and is created
via the function's parameter.

8. wait_time - Handles generating a random amount of time to wait for
for the tooth fairy ride. Created within the tooth_fairy() function
and can only be used there.

9. again - Handles if the user wants to go on another ride or not.
Created as a global variable that can be accessed by anything.

"""



#This is for choosing a random wait time for the tooth fairy ride
import random 

#Introduction
print("⣿⣿⣿⣿⣿⠟⠁⣠⣶⣦⣤⣶⣶⣶⣶⣤⣀⣀⣀⣈⠉⠁⣤⣤⣄")
print("⣿⣿⣿⡿⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢀⣼⣿⠿")
print("⣿⣿⣿⠁⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢀⠐⠈⢁⣀")
print("⣿⣿⠇⢀⣿⡿⠿⠛⠋⠉⠉⠉⢀⢀⣀⣀⣠⣤⣼⣷⣾⣿⣿⡿")
print("⠿⠏⢀⡾⢀⢀⣀⣀⣠⣤⣶⡶⠞⣿⣿⣉⡟⣬⢙⠿⣿⣿⠏⠁⣰")
print("⣤⣤⡴⣷⠛⣿⣿⣿⣿⣿⣿⠇⢀⠙⠻⢿⣿⣧⡾⠶⢻⠛⢀⣼⣿")
print("⠘⠻⢶⣯⡝⢠⣍⣻⣿⣿⠋⢀⢀⢀⢀⢀⢀⢀⢀⢀⡿⢀⣼⣿⣿")
print("⢀⢀⢀⠙⣟⠋⠉⠉⢀⢀⠠⠴⠖⠛⠉⢀⢀⢀⢀⣼⠁⣰⣿⣿⣿")
print("⢀⢀⢀⢀⠈⢧⣀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣠⠞⠁⣠⣿⣿⣿⣿")
print("⢀⢀⢀⢀⣠⣀⠈⠓⠦⣄⣀⣀⣀⣀⣤⣴⣾⠁⢠⣾⣿⣿⣿⣿⣿")
print("⢀⢀⢀⣸⣿⣿⣿⣦⣄⢀⢹⣿⣿⣿⣿⣿⣿⡆⠈⣿⣿⣿⣿⣿⣿")
print("⢀⢀⣼⣿⣿⣿⣿⣿⡏⢀⢸⣿⣿⣿⣿⣿⣿⣷⢀⢻⣿⣿⣿⣿⡟")
print("⢀⠘⠛⠛⠛⠛⠛⠛⢀⢀⠘⠛⠛⠛⠛⠛⠛⠛⠃⢀⠛⠛⠛⠛")
print("𝑺𝒂𝒓𝒗𝒆𝒔𝒉 𝑻𝒉𝒊𝒂𝒈𝒂𝒓𝒂𝒋𝒂𝒏 𝑷𝒓𝒆𝒔𝒆𝒏𝒕𝒔")
print("The 𝕵𝖆𝖑𝖊𝖇𝖎 𝖊𝖓𝖙𝖊𝖗𝖙𝖆𝖎𝖓𝖒𝖊𝖓𝖙 amusement system!")
print("-----------------------------------------")

#This function handles asking the users which ride they would like
#to go on. It also has error handling and gives feeds the acdec
#ride function the info it needs. It also handles 75% of the NSTEM 
#ride.

def question():
    while True:
        
        try:
            
            choice = int(input("-----------------------------------------\nWhich ride would you like to go on? 🤔 \n\nEnter,\n'1' for the stem hours ride: \n'2' for the acdec ride: \n'3' Tooth fairy simulator:\n"))
            if choice == 1:
                while True:
                    print("-----------------------------------------")
                    try:
                        hours = int(input("How many NSTEM hours do you have? \n"))
                        option = stem_hours_ride(hours)
                        while True:
                            if option == "hours_true":
                                life = input(str("\nDo you have a life?(Y/N): "))
                                if life == "Y" or life == "y":
                                    print("\n😭  You cannot go on this ride as you have a life!")
                                elif life == "N" or life == "n":
                                    print("\nHave fun! enjoy your ride!")
                                    break
                                else:
                                    print("\n😱  Invalid input. Enter Y or N \n-----------------------------------------")
                                    continue
                                break
                            elif option == "hours_false":
                                print("\n😭  Sorry, you can't go on this ride as you don't have enough stem hours")
                                break
                        break
                    except ValueError:
                        print("\n😱  Invalid input, Enter a number! ")
                        continue
                break
            
            elif choice == 2:
                print("-----------------------------------------\nFor this ride, you must have 3 people per Acdec team!\n")
                while True:
                    try:
                        ppl_count = int(input("How many people are in your team? "))
                        acdec_ride(ppl_count)
                        break
                    except ValueError:
                        print("\n😱  Invalid input, Enter a number! \n-----------------------------------------")
                        continue
                break
            
            elif choice == 3:
                tooth_fairy()
                break
            
            else:
                print("\n😱  Invalid input, Enter 1, 2 or 3.")
        
        except ValueError:
            print("\n😱  Invalid input, Enter 1, 2 or 3.")
            continue
        
#This function handles the Stem Hours ride, it checks if a user 
#has enough hours to ride it.
def stem_hours_ride(y):
    if y >= 120:
        return "hours_true"
    else:
        return "hours_false"

#This function handles the ACDEC ride, it checks if there are a 
#a good amount of people to make the ACDEC team for the ride.

def acdec_ride(x):
    while True:
        try:
            if x % 3 == 0:
                print("\nGreat! You will have " + str(x/3) + " teams!")
                break
            else:
                print("\n😭  Sorry, You can't go on this ride. You need a larger or \nsmaller team")
                break
        except ValueError:
            print("\n😱  Invalid input! Enter a whole number!")
            continue

#This function handles the tooth fairy ride and gives the user
#a random time to wait until the ride opens (I learnt this from
#going through the docs tab :D)
def tooth_fairy():
    wait_time = random.randint(1,60)
    print("-----------------------------------------\nAwesome choice! The wait time will be " + str(wait_time) + " minutes.")
    
print("Welcome to 𝕵𝖆𝖑𝖊𝖇𝖎 𝖊𝖓𝖙𝖊𝖗𝖙𝖆𝖎𝖓𝖒𝖊𝖓𝖙!")

question()

#This handles repeating the program if the user wants to book
#another ride
while True:
    again = input(str("-----------------------------------------\nWould you like to book another ride? (Y/N) "))
    if again == "n" or again == "N":
        print("\nAlright, thanks for coming to 𝕵𝖆𝖑𝖊𝖇𝖎 𝖊𝖓𝖙𝖊𝖗𝖙𝖆𝖎𝖓𝖒𝖊𝖓𝖙!")
        break
    elif again == "y" or again == "Y":
        question()
    else:
        print("\n😱  Invalid input. Enter Y or N ")
        continue
