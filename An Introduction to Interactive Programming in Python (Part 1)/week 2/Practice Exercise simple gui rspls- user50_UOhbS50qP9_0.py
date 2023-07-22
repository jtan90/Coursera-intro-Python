# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS
def name_to_number(name):
    if name == "Rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Invalid thing"
    
    # convert name to number using if/elif/else
    # don't forget to return the result!

def number_to_name(number):
    
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Invalid number"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
   
    print "Player chooses", player_choice  
    player_number = name_to_number(player_choice)
        
    import random
    comp_number = random.randint(0, 4)
    
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    
    compare = (comp_number - player_number) % 5
    
    if compare == 1:
        print "Computer wins!"
    elif compare == 2:
      print "Computer wins!"
    elif compare == 3:
        print "Player wins!"
    elif compare == 4:
        print "Player wins!"
    else:
        print "Player and Computer tie!"
   
    print ""
     
    
# Handler for input field
def get_guess(guess):
    if not (guess == "Rock" or guess == "paper" or guess == "scissors" +
        guess == "lizard" or guess == "Spock"):
        print
        print 'Error: Bad input "' + guess + '" to rpsls'
        return
    else:
        rpsls(guess)


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
