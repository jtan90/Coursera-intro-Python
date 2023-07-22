# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# write import statements
import math
import random
import simplegui

# define global variables
secret_number = 0
max_range = 100
max_guess = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, max_range, max_guess
   
    secret_mumber = random.randrange(0, max_range)
    max_guess = int(math.ceil(math.log((max_range), 2)))
    print"---------"
    print"---------"
    print "New game beings with a secret number from 0 to", str(max_range)
    print "Number of remaining guess is", str(max_guess)


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global max_range
    max_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    max_range
    max_range = 1000
    new_game
    
def input_guess(guess):
    global max_guess
    
    #print guess number
    guess = int(guess)
    print "Guess was", guess
    
    #print number of remaining guesses
    max_guess -= 1
    print "Number of remaining guesses is", max_guess
    
    #compare guess number with secret number
    if max_guess == secret_number:
        print "Correct!"
        new_game()
    else:
        if max_guess == 0:
            print "You ran out of guesses. The number was", secret_number
            new_game()
        else:
            if guess < secret_number:
                print "Higher"
            else:
                print "Lower"
            
    
# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess:", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
