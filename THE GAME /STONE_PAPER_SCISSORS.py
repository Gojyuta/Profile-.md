# ROCK PAPER SCISSORS THE GAME

import random 
    #Importing Random moudule for the game

choices = ("stone","paper","scisors") 
    # CHOICES THAT PLAYER & COMPUTER WOULD SELECT

comp = input("Set a name for your computer 1st: ".capitalize()).capitalize() 
    #custom computer name
Player_name = input("Set your name: ".capitalize()).capitalize()
    #Custom player name input



#HERE IT IS CHEATER GAMBLER ,WHO ALLOWS YOU TO CHEAT its upto you to play fair or just use him
def Cheat_code():
  No_msg = (("Tears loading… (left)"),("Couldn’t handle the pressure huh? (left)"),("That’s all it took? (left)"),("Rage quit moment? (left)"),("He saw the scoreboard and vanished (left)"),("Controller flew, didn’t it? (left)"),("Thought you had a chance… (left)"),("Game too real for him (left)"),("Logged off with ego bruised (left)"),("Quiet exit, no goodbye (left)"))
  Rand_No_msg= (random.choice(No_msg))
  
  
  GAMBLER = input("Do you want MY proffesional experience in this?\nIm a pro GAMBLER (Y/N)")
  if GAMBLER.lower() != "n":
    print (f"GAMBLER:  Lemme think...\nGAMBLER: Still thinking...\nGAMBLER: well well well, \nHe gonna choose {Comp.upper()} i can never be wronge\nso, choose your response according to it..\n \n ")
  else:
    print (f"GAMBLER :{Rand_No_msg} \n \n")



playing = True
win_lines = (
    f"omgggg, {Player_name} you won!!",
    f"No wayyyy, {Player_name} clutched it!!",
    f"Wooohooo, {Player_name} takes the W!!",
    f"Insaneee, {Player_name} is the champion!!",
    f"Bruhhh, {Player_name} really did that!!",
    f"Ayooo, {Player_name} with the dub!!",
    f"Sheeesh, {Player_name} just dominated!!",
    f"Let’s gooo, {Player_name} on top!!",
    f"Wait what?! {Player_name} actually won!!",
    f"Big W for {Player_name}!!",
    f"Yesssssir, {Player_name} with the win!!"
)

win_msg = (random.choice(win_lines))
try:
  while playing:
    
    player = None
    Comp = (random.choice(choices))
    Cheat_code()
    
    while player not in choices: #if player not choosed from choice it wont work
      player = input(f"Choose any 1 from {choices}").lower()
      if player.lower() not in choices:
        print ("wronge! input retry...\n \n")
        
      elif player == Comp:
        print (f"{comp} gone for : {Comp}")
        print ("Its a tie".title())
        
      elif player == "stone" and Comp == "scisors":
        print (f"{comp} gone for : {Comp}")
        print (win_msg)
        
      elif player == "scisors" and Comp == "paper":
        print (f"{comp} gone for : {Comp}")
        print (win_msg)
        
      elif player == "paper" and Comp == "stone":
        print (f"{comp} gone for : {Comp}")
        print (win_msg)
        
      else:
        print (f"{comp} gone for : {Comp}")
        print (f"Skill issues lil bro, {comp} won!")
        
    Play_again = input("Do you want to Play Again? (Y/N)").lower()
    if Play_again != "y":
      playing = False
except:
  print("----Some error occured!---")
  #If any mistype this will run
print ("Game Over")
