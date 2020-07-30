from graphics import *
import random
from button import Button
import time
from playsound import playsound
import math
import sys

score_label = Text(Point(70,60), "Score: 0")
score_label.setTextColor("white")
time_label = Text(Point(70,30), "Time Left: 100")
score_label.setSize(16)
time_label.setSize(16)
time_label.setTextColor("white")
puzzle_label = Text(Point(300,120), "Clue")
puzzle_label.setTextColor("white")
puzzle_label.setSize(16)

def introduction(win):
     
     """
     Sets up the objects on the first window
     Parameters:
                win, the window in which objects are drawn
     Return Value:
                None
     """
     
     playgame = Button(Rectangle(Point(160,135), Point(430,200)), Text(Point(0,0), "Play Game"))
     playgame.rect.setFill("white")
     Instructions = Button(Rectangle(Point(160,231), Point(430,296)), Text(Point(0,0), "Instructions"))
     Instructions.rect.setFill("white")
     Credits = Button(Rectangle(Point(160,327), Point(430,392)), Text(Point(0,0), "Credits"))
     Credits.rect.setFill("white")
     Quit = Button(Rectangle(Point(530,15), Point(590,45)), Text(Point(0,0), "Quit"))
     Quit.rect.setFill("red")
     
     Instructions.draw(win)
     Credits.draw(win)
     playgame.draw(win)
     Quit.draw(win)

def Credits():

     """
     Shows a Credits window to display the authors, etc. 
     """
     credit = GraphWin("Credits", 600 , 600)
     credit.setBackground("black")
     Credits_label = Text(Point(credit.getWidth()/2,123), """
This project was done by:
Ahmed Elsayed
Nadr Elhelu
Jeff Mutethia 
It was part of CS-167 project.
Credits given to graphics.py and playsound.py .""")
     
     Credits_label.setSize(18)
     Credits_label.setTextColor("white")
     Credits_label.draw(credit)
     while True:
          time.sleep(0.01)
         
          Credits_label.move(0,1)
          if Credits_label.getAnchor().getY() >= 800:
               credit.close()
               main()

def play_game():

     """
     Plays the game by adding score to 1st, 2nd, 3rd, 4th, and 5th clues.
     Parameters:
                 None
     Return Value:
                 None
     """
     
     score = 0
     Timer = 100
     Game = GraphWin("Criminal Case", 600 , 600)
     
     time_label.draw(Game)
     score_label.draw(Game)
     
     
     Game.setBackground("black")
     Set_up(Game)
     score += first_clue(Game, score)
     score += second_clue(Game, score)        
     third_clue(Game)
     score += fourth_clue(Game, score)
     score += fifth_clue(Game, score)
     win_game(Game, score) 
     
def Set_up(win):
     """
     Sets up the game by introducing the main purpose of the game
     Parameters: None
     Return Value: None 
     """
     Setup_message = "You are entering your sister's room. \n  She had told you that she got \n you a Christmas Present and you \n \
want to discover what did she \n order for you."
     Setup_label = Text(Point(300,300), Setup_message)
     Setup_label.setTextColor("white")
     Setup_label.setSize(16)
     Setup_label.draw(win)
     time.sleep(10)
     Setup_label.undraw() 
     
def first_clue(win, score):
     
     """
     Starts the first clue by asking the user to find an object on the screen
     Parameters:
                win, the window in which we are displaying objects
                score, the score of the player.
     Return value:
                  score 
     """
     
     Timer = 100
     picture = Image(Point(300,430), "messy_room.png")
     picture.draw(win)
     solved = False
     puzzle_label.setText("Puzzle: Your sister's room is VERY messy! \n \
Find an item that could help you get \n her online order.")
     puzzle_label.draw(win)
     
     while Timer > 0:
          pt = win.checkMouse()
          time.sleep(0.01)
          Timer -= 0.01
          time_label.setText("Time Left: " + str(math.trunc(Timer)))
          
          if pt != None:

               if (pt.getY() >= 255):
                    if (pt.getX() <=162 and pt.getX() >= 105 and pt.getY() <= 436 and pt.getY() >= 403):
                         print("You touched the laptop!")
                         score += 100
                         picture.undraw()
                         score_label.setText("Score: " + str(score))
                         solved = True
                         return score
               
                    else:
                    
                         score -= 20
                         score_label.setText("Score: " + str(score))
                         puzzle_label.setText("Wrong item!") 
                    
     if solved == False:
          
          print("Time is up. You lost! Your final score was", score)
          win.close() 
          sys.exit() 

def second_clue(win, score):
     
     """
     Starts the second clue by asking the user to find an object on a picture
     Parameters:
                win, the window in which we are displaying objects
                score, the score of the player
     Return value:
                score
     """
     
     print("We are at the second clue")
     solved = False
     time_label.setText("Time Left: 100")
     puzzle_label.setText("Congratulations! \n Your sister is very careful. \n \
She had chosen a very complicated password that \n you should \
decipher to access  \n the laptop")
     time.sleep(8)
     puzzle_label.setText("You should be able to input the password.")
     time.sleep(4)
     puzzle_label.setText("We should go to find something else to know the password")
     time.sleep(5)
     puzzle_label.setText("Puzzle: \n find a place that might contain anything \n to find a clue.") 
     picture = Image(Point(300,430), "messy_room.png")
     picture.draw(win)
     Timer = 100
     
     while Timer > 0:
          
          pt = win.checkMouse()
          
          time.sleep(0.01)
          Timer -= 0.01
          time_label.setText("Time Left: " + str(math.trunc(Timer)))
          
          if pt != None:
               
               if (pt.getY() >= 255):
                    if (pt.getX() <=211 and pt.getX() >= 189 and pt.getY() <= 480 and pt.getY() >= 435):
                         print("You found the correct item!")
                         score += 100
                         picture.undraw()
                         score_label.setText("Score: " + str(score))
                         solved = True
                         return score
               
                    else:
                    
                         score -= 20
                         score_label.setText("Score: " + str(score))
                         puzzle_label.setText("Wrong item!")
                       
     if solved == False:
          
          print("Time is up. You lost the case! Your final score was", score)
          win.close()
          sys.exit() 

          
     

     return score

def third_clue(win):

     """
     Starts the third clue by showing the user a screen and asking them to use the notes to solve the code
     Parameters:
                win, the window in which objects are displayed
     Return Value:
                None 
     """
     
     print("We are at the third clue!")
     solved = False
     time_label.setText("Time Left: 15")
     puzzle_label.setText("Congratulations! \n Now we should read the notes and figure out the password \n you only have 15 seconds.")
     time.sleep(5)
     picture = Image(Point(300,430), "third_clue.png")
     picture.draw(win)
     Timer = 15
     while Timer > 0: 
          time.sleep(0.01)
          Timer -= 0.01
          time_label.setText("Time Left: " + str(math.trunc(Timer)))
     picture.undraw()

def fourth_clue(win, score):
     
     """
     Starts the fourth clue, where the user is required to enter a code in an Entry Object
     Parameters:
                win, the windows in which objects are displayed
                score, the score of the player
     Return Value:
                  score 
     """
     
     print("We are the fourth clue!")
     solved = False
     time_label.setText("Time Left: 100")
     puzzle_label.setText("Figure out the password based \n on the notes you have taken")
     Password_Box = Entry(Point(250,300), 5)
     Password_Box.setSize(20)
     Enter_Password = Button(Rectangle(Point(300,278), Point(500,322)), Text(Point(0,0), "Enter Password"))
     Enter_Password.rect.setFill('white')
     Password_Box.draw(win)
     Enter_Password.draw(win)
     Timer = 100
     
     while Timer > 0:
          
          pt = win.checkMouse()
          time.sleep(0.01)
          Timer -= 0.01
          time_label.setText("Time Left: " + str(math.trunc(Timer)))
          
          if pt != None:
               
               if (pt.getX() <=500 and pt.getX() >= 300 and pt.getY() <= 322 and pt.getY() >= 278):
                    
                    Password_Text = Password_Box.getText()
                    
                    if Password_Text == "123":
                         
                         score += 100
                         Password_Box.undraw()
                         Enter_Password.rect.undraw()
                         score_label.setText("Score: " + str(score))
                         solved = True
                         puzzle_label.setText("Congratualtions you cracked the code!")
                         return score
                    
                    else:
                         
                         Password_Box.setText("")
                         score -= 20
                         score_label.setText("Score: " + str(score))
                         puzzle_label.setText("Wrong Password!")
                         
     if solved == False:
          print("Time is up! You lost! Your final score is", score)
          win.close()
          sys.exit()  
                         
def fifth_clue(win, score):

     """
     Starts the final clue, where the user is asked to use piano keys to solve a puzzle
     Parameters:
                win, the windows in which objects are displayed
                score, the score of the player
     Return Value:
                  score 
     """
     
     picture =  Image(Point(300,430), "pianokeys.png")
     time_label.setText("Time Left: 100")
    
     puzzle_label.setText("There is a second-step authentication password \n using the piano keys")
     time.sleep(5)
     puzzle_label.setText("You have to type the keys corresponding to \n each key.")
     time.sleep(5)
     puzzle_label.setText("Play notes that corrosponds the keys on \n the keyboard.")
     time.sleep(4)
     puzzle_label.setText("Enter three keys at a time")
     time.sleep(4)
     puzzle_label.setText("A place at Whitman, three-letters \n behind reid, on main \n a place of glover.")
     time.sleep(3)
     Timer = 100
     picture.draw(win) 
     solved = False
     password = ''
     
     while Timer > 0:
          time.sleep(0.01)
          Timer -= 0.01
          time_label.setText("Time Left: " + str(math.trunc(Timer)))
          key = win.checkKey()
          
          if key != '':
               
               if key == 'a':
                    password += 'a'
                    playsound("A.wav")
               elif key == 'b':
                    password += 'b'
                    playsound("B.wav")
               elif key == 'c':
                    password += 'c'
                    playsound("C.wav")
               elif key == 'd':
                    password += 'd'
                    playsound("D.wav")
               elif key == 'e':
                    password += 'e'
                    playsound("E.wav")
               elif key == 'f':
                    password += 'f'
                    playsound("F.wav")
               elif key == 'g':
                    password += 'g'
                    playsound("G.wav")
               else:
                    puzzle_label.setText("Only type the keys on the picture")
                    
                    
               if len(password) == 3:
                    if password == 'gac':
                         score += 100
                         picture.undraw()
                         score_label.setText("Score: " + str(score))
                         puzzle_label.setText("Congratualtions! You finally opened the laptop! \n Let's discover what your gift is!")
                         time.sleep(4)
                         return score
                    else: 
                         password = ''
                         score -= 50
                         puzzle_label.setText("Wrong Password! \n A place at Whitman, three-letters \n behind reid, on main \n a place of glover")
                         score_label.setText("Score: " + str(score))

     
     if solved == False:
          print("Time is up! You lost! Your final score is", score)
          win.close() 
          sys.exit() 
          
     return score
     
def win_game(win, score):
     
     picture = Image(Point(300,400), "gift.png")
     Win_label = Text(Point(300,300), "Congratulations!! You have won with a score of \n" + str(score))
     Win_label.setTextColor("white")
     Win_label.setSize(16)
     Win_label.draw(win)
     Win_label.move(0,-200)
     time_label.undraw()
     score_label.undraw()
     time.sleep(5)
    
     Win_label.setText("Merry Christmas! She got you nothing!")
     picture.draw(win)
     


def main():
     
     win = GraphWin("Christmas Gift!", 600, 500)
     win.setBackground("black")
     introduction(win)
     
     while True:
          choice = win.getMouse()
          if choice.getX() <= 430 and choice.getX() >= 160 and choice.getY() >= 135 and choice.getY() <= 200:
               win.close()
               play_game()
               break
          elif choice.getX() <= 430 and choice.getX() >= 160 and choice.getY() >= 231 and choice.getY() <= 296:
               win.close()
               Instructions()
               break
          elif choice.getX() <= 430 and choice.getX() >= 160 and choice.getY() >= 327 and choice.getY() <= 392:
               win.close()
               Credits()
               break
          elif choice.getX() <= 590 and choice.getX() >= 530 and choice.getY() <= 45 and choice.getY() >= 15:
               print("GoodBye!")
               win.close()
               break
     

     

if __name__ == "__main__":
     main()

