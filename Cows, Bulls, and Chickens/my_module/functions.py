#Importing packages
import random
import os
import pickle

class UserID:
    '''This class contains methods that assist the Cows, Bulls, and Chickens game. With this class, we are keeping track of the objects name and counter of the number of tries the player takes to get the correct guess. This class also stores player user names in a file 'UserID.txt'
    '''
    
    def __init__(self):
        
        #Instance variables
        self.name = ""
        self.counter = 0
        self.dict_user_ID = {}
    
    def file_creation(self):
        '''This method is called to create a file named 'UserID.txt' which will store the dictionary data of user names. This method checks if the file already exists at the path. If it does, then it doesn't override and create another file, and if it does not, it creates the file.
        '''
        
        current_dir = os.getcwd()

        if os.path.isfile(current_dir + "/UserID.txt"):
            pass
        
        else:
            #Creating the file with an empty dictionary
            self.dict_user_ID = {}
            result = open('UserID.txt', 'wb')
            pickle.dump(self.dict_user_ID, result)
            result.close()    
    
    def user_ID(self):
        '''This method updates the instance variable dictionary dict_user_ID and updates the file 'UserID.txt' depending on the response of the user. If the user is a repeating user, then it welcomes the user, else, it prompts the user to input their user name
        '''
        
        yes_no = input("Are you a first time user? Please type in y or n: ")
        
        while True:
            
            #If input is "y" or yes
            if yes_no == "y":
                
                #Reading the file
                file_load = open('UserID.txt', 'rb')
                
                #Storing the existing dictionary data onto dictionary instance variable dict_user_ID
                self.dict_user_ID = pickle.load(file_load)
                file_load.close()
                
                #Obtaining user name
                name = input("Please type a user name of your choice: ")
                self.name = name
                length = len(self.dict_user_ID)
                
                #Updating dictionary with first-time user's name and key being length+1 (key starts from 1)
                self.dict_user_ID.update({length+1:self.name})
            
                #Obtaining current working directory
                current_dir = os.getcwd()
            
                #Writing back to the file 'UserID.txt' by dumping the updated dictionary
                file_load = open("UserID.txt", "wb")
                pickle.dump(self.dict_user_ID, file_load)
                file_load.close()
                
                #Breaking from the loop if it is a first-time user
                break

            #If input is "n" or no
            elif yes_no == "n":
                
                #Obtaining user name
                given_ID = input("What is your user name? ")
                self.name = given_ID
                
                #Calling the confirm_ID method to confirm whether the user ID inputted is already in the database
                bool_ID = self.confirm_ID(given_ID)

                #If it is, we greet the user
                if bool_ID == True:
                    print("Welcome back " + str(self.name) + "!")
                    break

                #else, we prompt the user to type input their user name again
                else:
                    print("Sorry, we could not find your name/ID.")
                    yes_no = input("Are you a first time user? Please type in y or n: ")
            
            #If the input is not a "y" or "n"
            else:
                #prompting the user again
                yes_no = input("Try again. Are you a first time user? Please type in y or n: ")

    def confirm_ID(self, given_ID):
        '''This method checks whether the input string given_ID is in the file 'UserID.txt'. It returns True if it is, False if not
        '''
        
        #Reading the file data into the dictionary
        file_load = open("UserID.txt", "rb")
        self.dict_user_ID = pickle.load(file_load)
        file_load.close()
        
        #Looping through the dictionary
        for x in self.dict_user_ID.keys():
            
            if given_ID in self.dict_user_ID[x]:
                return True

        else:
            return False

        
def prompt_user(lev):    
    '''This method prompts the user for the number of tries, categorizes the number of tries by level, and ensures that the input is an integer
    
    Raises
    _______
    
    ValueError:
        Raises ValueError if the input is not an integer
    '''
    
    #Setting an itital value to the local variable
    return_val = ""
    
    while True:
        try:
            #Checks if lev is an int
            lev = int(lev)
            
            #Breaking out of the while loop if there is no ValueError thrown
            break

        except ValueError:
            #Re-prompting the user
            print("Invalid input. Please type an integer")
            lev = input("How many tries would you like? ")

    #Categorizing lev into different levels of difficulty
    if type(lev) == int:
        
        if lev < 15:
            return_val = "Advanced"

        elif lev >= 15 and lev < 30:
            return_val = "Medium"

        else:
            return_val = "Beginner"
    
    print("You are in the " + str(return_val) + " level and get " +  str(lev) + " tries!")
    
    #returning the value of lev
    return lev

def play():
    '''This method acts like our main method to play the game!
    '''
    
    print("Welcome to Cows, Bulls, and Chickens! Guess a random 4 digit number to play the game! Type in STOP to quit the game")
    
    lev = input("How many tries would you like? ")
    
    #Prompting the user by calling the prompt_user method
    lev = prompt_user(lev)
    
    #Making a player object of the UserID class
    player = UserID()
    
    #Creating a file and checking if the user is a first-time user or not after this method is called, you should notice a new file named 'UserID.txt' in your project folder
    player.file_creation()
    player.user_ID()
    
    #Generating a random 4 digit number as the correct value number to be guessed
    cor_val = str(random.randint(1000,9999))
    
    #Looping through the number of tries inputted by the user
    for item in range(0, int(lev)):
        
        #Resetting values each time the loop restarts
        cows = 0
        bulls = 0
        inc = 0
        draft_chicken = []
        chickens = []
        chicken = 0
        
        #Asking for the guess - a 4 digit number
        guess = input("Guess a four digit number: ")
        
        #List of all valid integer input
        list_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            
        #Stop command used to quit the game
        if guess == "stop" or guess == "STOP":
            
            #Quitting the game with the final answer
            final_string = "The correct answer is: " + str(cor_val)
            return final_string
        
        while True:
            
            #Checking if the input is a valid 4 digit int instead of a string or a different number of digits
            for a in guess: 
                if a not in list_num:
                    
                    print("Invalid input. Please type an integer. ")
                    guess = input("Guess a four digit number: ")
                    break
                        
                elif len(guess) != 4:
                    print("Invalid input. Please type an integer. ")
                    guess = input("Guess a four digit number: ")

            else:
                break
        
        #If the user gets the correct guess
        if guess == cor_val:
            break

        for j in range(0, len(cor_val)):
            for i in range(0, len(guess)):

                #Updating cows, bulls, and chicken values based on guess and correct number
                
                #Checks for digits in the correct position
                if guess[i] == cor_val[j] and i == j:
                    cows += 1

                #Checks for digits in the wrong position
                elif guess[i] != cor_val[j] and i == j:
                    bulls += 1

                #Checks if the digits are correct irrespective of their position
                if guess[i] == cor_val[j]:
                    draft_chicken.append(guess[i])
                    
                    for k in draft_chicken:
                        if k not in chickens:
                            chickens.append(k)

        inc = len(chickens)
        chicken = chicken + int(inc)

        #Printing out the number of cows, bulls, and chickens
        print(f"cows: {cows}, bulls: {bulls}, chickens: {chicken}")
        
        #Incrementing counter with each guess/try
        player.counter += 1

    #Printing this message after the player gets the correct guess
    print("You took " + str(player.counter) + " tries.")
    print("The correct answer is " + str(cor_val))