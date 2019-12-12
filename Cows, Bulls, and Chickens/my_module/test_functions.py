from functions import UserID
import os.path

def test_function():

    assert UserID()
    player = UserID()
    
    #Testing if the file "UserID.txt" is being created
    assert player.file_creation() == None

    #Calling the above method will create a file named "UserID.txt".
    #For testing sake, we do not need this file
    os.remove("UserID.txt")

    #Checking if the instance variables are correct
    assert player.dict_user_ID == {}
    assert player.name == ""
    assert player.counter == 0
    
test_function()