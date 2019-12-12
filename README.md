#### Author: Divya S K

# Project Description

This project is a take on the classic game Cows and Bulls called Cows, Bulls, and Chickens. In this game, the user has to guess a four digit number from using the Cows, Bulls, and Chickens cues in a specific number of tries. The aim of this project is to minimize the number of tries required to guess the correct number. Here is what each cue stands for:

## Cows:
This is the number of digits which are in the correct position

## Bulls:
This is the number of digits which are not in the correct position

## Chickens:
This is the number of digits that are present in the number but could be in the wrong position

### Example:
Let us say that the randomly-generated, correct number is 2389

If you guess 2090, the output will be:
cows: 1, bulls: 3, chickens: 2

Here there is 1 cow because 2 is in the correct position while the rest are not. There are 3 bulls because 3 of the digits are not in the right position. There are 2 chickens as two of the digits are present in the correct number but could be in the wrong position.


The player can also create and play under their username, which is implemented with the help of pickle library and the information is stored in a file named 'UserID.txt'. If there is a repeating user, the code welcomes the user. 
