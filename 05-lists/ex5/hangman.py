import turtle
import random

t = turtle
screen = turtle.getscreen()

def initialize(): #This sets up the background and settings for the game
    global word
    t.speed(0) #This creates the settings
    screen.tracer(0)
    t.hideturtle()
    t.setworldcoordinates(20,20,80,80)

    t.penup() #This draws a gallow
    t.setpos(55,45)
    t.pendown()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(5)

    t.penup()
    t.setpos(35,30)
    t.left(90)
    for i in range(len(word)): #This draws the underscores for letters
        t.pendown()
        t.forward(2)
        t.penup()
        t.forward(2)

def drawLetter(word,character): #Called when player correctly guesses. Draws letter
    global count
    times = [x for x, appearance in enumerate(word) if appearance == character] #Creates list of when 'character' appears in 'word'
    for i in range(len(times)): #Draws character based on when it appears in 'word'
        t.penup()
        t.setpos(36 + 4*(times[i]),31)
        t.write(character, move=True, align='center', font=('Arial', 20, 'normal'))
    count += len(times)

def drawBody(): #Called when player incorrectly guesses. Draws body part
    global n
    t.setheading(270)
    t.penup()
    if n == 0: #draws head
        t.setpos(45,60)
        t.right(90)
        t.pendown()
        t.circle(3,360,500)
        t.penup()
    elif n == 1: #draws torso
        t.setpos(45,54)
        t.pendown()
        t.forward(8)
        t.penup()
    elif n == 2: #draws left arm
        t.setpos(45,51)
        t.right(135)
        t.pendown()
        t.forward(6)
        t.penup()
    elif n == 3: #draws right arm
        t.setpos(45,51)
        t.left(135)
        t.pendown()
        t.forward(6)
        t.penup()
    elif n == 4: #draws left leg
        t.setpos(45,46)
        t.right(45)
        t.pendown()
        t.forward(6)
        t.penup()
    elif n == 5: #draws right leg
        t.setpos(45,46)
        t.left(45)
        t.pendown()
        t.forward(6)
        t.penup()

def guess(): #This function asks the user for an input, and either draws a body part or a letter
    global word
    global n
    character = t.textinput('Your Guess','What letter are you thinkin\'')
    if character in word: #If letter is in word, draws letter
        drawLetter(word,character)
    else: #If letter not in word, draws body part
        drawBody()
        n += 1

def fake_main():
    global n
    global count
    global word
    n = 0
    count = 0
    initialize()
    done = False
    while not done:
        if n > 5:
            done = True
            t.penup()
            t.setpos(50,70)
            t.write('You lose.' + 'The word was \'' + word + '\'', move=True, align='center', font=('Arial', 50, 'normal'))
        elif count > len(word) - 1:
            done = True
            t.penup()
            t.setpos(50,70)
            t.write('Amazing! You guessed the word \'' + word + '\'. You win!', move=True, align='center', font=('Arial', 30, 'normal'))
        else:
            guess()
    return None

def main():
    finished = False
    while not finished:
        global word
        wordList = ['lildicky','kendrick','jcole','eminem','kanye','bigsean','travis','childish','vicmensa','drake','weeknd','twochainz','ishdarr','asaprocky','schoolboy','kidcudi','chance','migos','wakaflame','guccimane']
        word = wordList[random.randint(0,19)]
        fake_main()
        repeat = t.textinput('','Would you like to play again? (y/n): ')
        if repeat == 'y':
            t.reset()
        else:
            finished = True
    return None

main()
