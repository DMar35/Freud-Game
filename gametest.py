import turtle
screen = turtle.Screen()


def print_finalscores():
  print("Final Stats:\n Id Score = " + str(IdCounter) + "\n Ego Score = " + str(Ego) + "\n Superego Score = " + str(SuperEgo) + "\n")
  print("Thanks for playing!")
  return

# Setup
yes_no = ["yes", "no", "Yes", "No"]
go_stay = ["Go", "go", "Stay", "stay"]
help_dont = ["Help", "help", "Don't", "don't"]
leave_stay_bring = ["Leave", "leave", "Stay", "stay", "Bring", "bring"]
watch_dont = ["Watch", "watch", "Homework", "homework"]
sleep_homework = ["Sleep", "sleep", "Homework", "homework"]
Decision_1 = ["Party", "party", "Study", "study"]
ego_list = ["Ego", "ego", "Id", "ID", "id", "superego", "Superego"]
IdCounter = 0
SuperEgo = 0
Ego = 0
scenario = ""
trueage = 0


  


name = input("Hello what is your name?\n")
print("Welcome " + name + "\n")

print("It is a Thursady night, beautifal weather and made to have fun in.")
print("You were invited to this crazy, once in a lifetime, party by your best friend, however you have a homework assignment due on Saturday and have to make a decision to go to the party or stay and do your homework even though it is not due until Saturday\n")

response = ""
while response not in Decision_1:
  response = input("What do you do?\nParty/Study\n")
  if response == "Party" or response == "party":
    print("To the party we go! I can start the homework tomorrow.\n")
    IdCounter += 1
    scenario = "Party"
  elif response == "Study" or response == "study":
    print("Better that I stay in and start my homework.\n")
    SuperEgo += 1
    scenario = "Study"
  else:
    print("Still thinking.\n")


response = ""
if scenario == "Party":
  screen.setup(600, 400)
  screen.bgpic("PixelParty.gif")
  print("You arrive at the party and are about to head in before a couple of guys come up to you and ask:")
  while True:
      age = int(input("How old are you?\n"))
      trueage = age
      if age >= 16:
        break
      else:
        print("Too young. Try again.")
  
  print("They let you into the party regardless.\n")
  print("You are now in the party and someone comes up to you asking if you want a drink.\n")
  response = ""
  while response not in yes_no:
    response = input("Do you accept the drink?\nYes/No\n")
    if age < 21 and (response == "yes" or response == "Yes"):
      IdCounter += 2
      print("Underage drinking... *Gulp... Gulp... Gulp*.\n")
    elif age >= 21 and (response == "yes" or response == "Yes"):
        IdCounter += 1
        print("Drink responsibly... *Gulp... Gulp... Gulp*.\n")
    elif response == "No" or response == "no":
        SuperEgo += 1
        print("Better to be responsible\n")
    else: 
        print("I didn't understand that.\n")
  
  print("As the party rages on, the music still ever so loud, the lights still bright, one of the party hosts wants to pull a prank on one of the guests.")
  print("The host of the party promises you that you have access to every party he throws ever again if you help him.\n")
  response = ""
  while response not in help_dont:
    response = input("Tempting offer... should I help him?\nHelp/Don't\n")
    if response == "Help" or response == "help":
      IdCounter += 1
      print("Woooooo... free party passes!\n")
    elif response == "Don't" or response == "don't":
      SuperEgo += 1
      Ego += 1
      print("I can't, I would feel super bad\n")
      
      print("*You are kicked out of the party*\n")
      screen.setup(500, 288)
      screen.bgpic("PixelStudy.gif")
      print("You head home and have two options. Start the assignment or sleep.")
      response == ""
      while response not in sleep_homework:
        response = input("Start the assignment or sleep\nHomework/Sleep\n")
        if response == "Sleep" or response == "sleep":
          IdCounter += 1
          print("You fall asleep for the night... *zzz...zzz...zzz...*\n")
          screen.setup(500, 507)
          screen.bgpic("PixelSleep.gif")
          print_finalscores()
          quit()
        elif response == "Homework" or response == "homework":
          SuperEgo += 1
          screen.setup(500, 288)
          screen.bgpic("PixelStudy.gif")
          print("Let's get crackin on this homework!\n")
          print("A couple of minutes pass by and you start getting hungry.\n")
          while response not in yes_no:
            response = input("Get a piece of candy to help satisfy my hunger?\nYes/No\n")
            if response == "Yes" or response == "yes":
              IdCounter += 1
              print("*Nom nom nom nom...*\n")
            elif response == "No" or response == "no":
              SuperEgo += 1
              print("Better to be healthy.\n")
            else:
              print("I can't hear myself over my hunger.\n")
        print("A couple of hours go by and you are really progressing well into your assignment when you realize what time it is...\n")
        print("It's time for the season finale of your favorite show! You really want to watch but also want to finish your homework.\n")
        print("You think to yourself, it isn't due until Saturday so I do have time. But what should I do?\n")
        response = ""
        while response not in watch_dont:
          response = input("Should I take a small break and watch the season finale of my favorite show?\nWatch/Homework\n")
          if response == "Watch" or response == "watch":
            IdCounter += 1
            print("Eh... an hour break is not going to hurt.\n")
            print("You end up falling asleep during the show.\n")
            screen.setup(500, 507)
            screen.bgpic("PixelSleep.gif")
            print_finalscores()
            quit()
          elif response == "Homework" or response == "homework":
            SuperEgo += 1
            print("I have to finish this\n.")
            print("You end up finising the assignment and fall asleep right after\n.")
            screen.setup(500, 507)
            screen.bgpic("PixelSleep.gif")
            print_finalscores()
            quit()
          else:
            print("What should I do?")
          
    else:
      print("Sorry, I couldn't hear you?")
  
  print("It is getting later in the night and you realize you have a heavy class load tomorrow. You have to decide whether you should stay or go\n")
  response = ""
  while response not in go_stay or response not in sleep_homework:
    response = input("Do I stay or do I go?\nStay/Go\n")
    if response == "Stay" or response == "stay":
      IdCounter += 1
      print("Party ON!\n")
      print("A couple hours pass when you start to hear sirens screeching around you.")
      print("The cops are here!\n")
      print("Unfortunately you get caught and are taken to the police station")
      print("All you can think is NO, NO, NOOOOOOOOOOOOOO!")
      print("You wake up from the nightmare that just took place. What were you thinking you think to yourself.\n")
      print_finalscores()
      print("Maybe next time, you should listen to your Superego")
      quit()
  
    elif response == "Go" or response == "go":
      screen.setup(500, 288)
      screen.bgpic("PixelStudy.gif")
      SuperEgo += 1
      print("Uhhhh... I have to go, I got to be responsible\n")
      print("You head home and it is about 11:00PM. Should I go to sleep or start the homework?\n")
      response = ""
      while response not in sleep_homework:
        response = input("Sleep or homework?\nSleep/Homework\n")
        if response == "Sleep" or response == "sleep":
          IdCounter += 1
          print("You fall asleep for the night... *zzz...zzz...zzz...*\n")
          screen.setup(500, 507)
          screen.bgpic("PixelSleep.gif")
          print_finalscores()
          quit()
        elif response == "Homework" or response == "homework":
          SuperEgo += 1
          print("You start the assignment but soon quickly fall asleep from all the partying you have done.\n")
          screen.setup(500, 507)
          screen.bgpic("PixelSleep.gif")
          print_finalscores()
          quit()
        else:
          print("What am I doing(Choices are sleep/homework)")
          
    else:
      print("Hmmm... what should I do.")
  
  
  
  
  
else:
  screen.setup(500, 288)
  screen.bgpic("PixelStudy.gif")
  print("*In your mind* You did the responsible thing staying to get a good start on that homework.\n")
  print("A couple of minutes pass by and you start getting hungry.\n")
  response = ""
  while response not in yes_no:
    response = input("Get a piece of candy to help satisfy my hunger?\nYes/No\n")
    if response == "Yes" or response == "yes":
      IdCounter += 1
      print("*Nom nom nom nom...*\n")
    elif response == "No" or response == "no":
      SuperEgo += 1
      print("Better to be healthy.\n")
    else:
      print("I can't hear myself over my hunger.\n")
  
  print("A couple of hours go by and you are really progressing well into your assignment when you realize what time it is...\n")
  print("It's time for the season finale of your favorite show! You really want to watch but also want to finish your homework.\n")
  print("You think to yourself, it isn't due until Saturday so I do have time. But what should I do?\n")
  response = ""
  while response not in watch_dont:
    response = input("Should I take a small break and watch the season finale of my favorite show?\nWatch/Homework\n")
    if response == "Watch" or response == "watch":
      IdCounter += 1
      print("Eh... an hour break is not going to hurt.\n")
    elif response == "Homework" or response == "homework":
      SuperEgo += 1
      print("I have to finish this.")
    else:
      print("What should I do?")
  
  print("An hour passes by, and it is MIDNIGHT when you get a call from your friend who invited you to the party.\n")
  print("He asks you if you can pick him up from the party as he is a little buzzed.\n")
  print("You think to yourself that it is quite late but at the same time, you don't want anything bad to happen to your friend.")
  response = ""
  while response not in go_stay:
    response = input("Should I go pick him up or should I stay here.\nGo/Stay\n")
    if response == "Go" or response == "go":
      Ego += 1
      print("Let's go, I don't want anything bad to happen to my friend.\n")
    elif response == "Stay" or response == "stay":
      print("He will be fine, he can just call an uber.")
      print("As the hours pass by, you end up just falling asleep.")
      screen.setup(500, 507)
      screen.bgpic("PixelSleep.gif")
      print_finalscores()
    else:
      print("What should I do?")
  
  print("You drive over to the party to pick up your friend and he greets you outside as you arrive.")
  screen.setup(600, 400)
  screen.bgpic("PixelParty.gif")
  print("Although you are here just to pick him up, he urgers you to stay at the party for a little bit.")
  print("You think to yourself what you should do.\n")
  response = ""
  while response not in leave_stay_bring:
    response = input("Should I stay, leave him here to do what he wants, or make sure to take him home now as a good friend?\nStay/Leave/Bring\n")
    if response == "Stay" or response == "stay":
      IdCounter += 1
      print("Woooo party!!!")
      print("You stay the night after doing a great job to start your homework. Well deserved\n")
      print_finalscores()
    elif response == "Leave" or response == "leave":
      SuperEgo += 1
      print("I'm leaving. Feel free to stay, but I am going home buddy.\n")
    elif response == "Bring" or response == "bring":
      Ego += 1
      print("Listen we should go, its been a long night for you my friend.\n")
      print("*You end up bringing your friend home*\n")
    else:
      print("Still thinking...")
  
  print("You arrive home and its nearly 1:00AM and you have a little bit left of the assignment.\n")
  print("Should I finish the assignment, or go to sleep? Considering how long the day has been I am really tired but it would be sweet to finish the assignment.\n")
  screen.setup(500, 288)
  screen.bgpic("PixelStudy.gif")
  response = ""
  while response not in sleep_homework:
    response = input("Go to sleep or finish the assignment?\nSleep/Homework\n")
    if response == "Sleep" or response == "sleep":
      IdCounter += 1
      screen.setup(500, 507)
      screen.bgpic("PixelSleep.gif")
      print("You fall asleep for the night... *zzz...zzz...zzz...*\n")
      print_finalscores()
    elif response == "Homework" or response == "homework":
      SuperEgo += 1
      print("You did it! You finally finished the assignment. Now time to go to sleep.\n")
      screen.setup(500, 507)
      screen.bgpic("PixelSleep.gif")
      print_finalscores()
    else:
      print("What am I doing(Choices are sleep/homework)")
  






"""screen = Screen()
t1 = Turtle("turtle", visible = False)
t2 = Turtle(shape = "turtle", visible = False)

# this assures that the size of the screen will always be 400x400 ...
screen.setup(400, 400)
screen.addshape("200pixv2.png")
t1.setpos(200,200)
t1.shape("200pixv2.png")
screen.addshape("200pixv11.jpg")
t2.setpos(200, 200)
t2.shape("200pixv11.jpg")"""
