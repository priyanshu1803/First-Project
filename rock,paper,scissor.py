import random
def game(computer,player1):
    if (computer==player1):
        return None
    elif (computer=='r'):
        if (player1=='p'):
           return True
        if (player1=='s'):
           return False   
    elif (computer=='p'):
        if (player1=='s'):
           return True
        if (player1=='r'):
           return True   
    elif (computer=='s'):
        if (player1=='p'):
           return False
        if (player1=='r'):
           return True
print("computer choice:rock('r'),paper('p'),scissor('s')")
a=random.randint(1,3)
if (a==1):
    computer='r'
elif (a==2):
    computer='p'                
elif (a==3):
    computer='s'
player1=input("enter your choice:\n")
c=game(computer,player1)
print(f"computer choice is {computer}")
print(f"player's choice is {player1}")
if (c==None):
    print("TIE!")
elif c:
    print("YOU WON!!")
else:
    print("YOU LOSE!")       