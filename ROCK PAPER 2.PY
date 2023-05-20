import random
l=["rock","scissor","papper"]
while True:
  ucount=0
  ccount=0
  uc=int(input('''Game start
  1=yes
  2=no'''))
  if uc==1:
    for i in range(1,6):
      user_i=int(input('''
        1=rock
        2=scissor
        3=papper   
                   '''))
      if user_i==1:
         uchoice="rock"
      elif user_i==2:
         uchoice="scissor"
      elif  user_i==3:
         uchoice="papper"
      cchoice=random.choice(l)  
      if cchoice==uchoice:
         print("user value",uchoice)
         print("computer value",cchoice)
         print("Game draw")
         ucount+=1
         ccount+=1
      elif (uchoice=="papper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="papper") or (uchoice=="rock" and cchoice=="scissor"):
        print("user value",uchoice)
        print("computer value",cchoice)
        print("user win")
        ucount+=1
      else:
        print("user value",uchoice)
        print("computer value",cchoice)
        print("computer win")
        ccount+=1
    if ucount==ccount:
     print("count of user is",ucount,"count of computer is",ccount) 
     print("Game draw")
    elif ucount>ccount:
     print("count of user is",ucount)
     print("User win")
    else:
     print("count of computer is",ccount)
     print("computer win")  
     print("do you want to play again")       
       
  else:
    break