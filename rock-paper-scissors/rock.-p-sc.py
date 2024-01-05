rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
def show(s : str, opt : int):
    print(f"{s} option:")
    print(f"{options[opt]}")
def wins():
    print("You win !!")
    
def lose():
    print("CPU wins, you lose")

import random as rd 
options = {1: rock, 2 : paper, 3: scissors}

print(rock)
print(paper)
print(scissors)
player = int(input("select anything, 1 for rock, 2 for paper and 3 for scissors"))
while(not player in [1,2,3]):
    player = int(input("Unvalid option, try again"))
show("Your", player)
cpu = rd.randint(1,3)
show("CPU", cpu)

if player == cpu:
    print("Its a draw!")
elif player == 1 and cpu == 3:
    wins()
#cubrir los extremos con condiciones
elif player == 3 and cpu == 1:
    lose()
elif player > cpu:
    #el sjug es tijera, le gana al papel y la opcion
    # de piedra por parte del cpu queda descartad
    wins()
elif cpu > player:
    lose()

