import random



R = "rock"
P = "paper"
S = "scissors"
x = input("Rock, Paper, Scissors. GO! ")



list1 = ["paper", "rock", "scissors"]
j = random.choice(list1) ; print(j)


if x == j:
  print("tie!")
print(" ")




if j == "paper" and x == "rock":
  print("loser")
print(" ")

if j== "rock" and x== "paper":
  print("aye winner")
print(" ")

if j == "scissors" and x == "paper":
  print("YOU LOST!")
P

if j == "paper" and x == "scissors":
  print("lets go u win!")
P

if j == "rock" and x == "scissors":
  print("you suck ass lmao")
P

if j == "scissors" and x =="rock":
  print("winner YAY")
P
input()
