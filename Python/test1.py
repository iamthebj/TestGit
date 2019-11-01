#importing the time module
import time

#welcoming the user
name = raw_input("What is your name? ")

print "Hello, " + name, "Time to play hangman!"

print "ss"

#wait for 1 secon

    print

    # ask the user go guess a character
    guess = raw_input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print "Wrong
"    
 
    # how many turns are left
        print "You have", + turns, 'more guesses' 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Loose"
            print "You Loose
"  
