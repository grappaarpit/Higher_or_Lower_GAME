from art import logo
from art import vs
from game_data import data
from random import randint
import os
# Show Graphics
print(logo)
A = []
B = []
C = []
score = 0
index_A = 0
index_B = 0

# PICK A
def compare_a():
  global A 
  global index_A

  A.clear()
  random = randint(0,49)
  index_A = random
  
  for i in data[index_A]:
    A.append(data[index_A][i])
  
  return A

# PICK B
def compare_b():
  global B 
  global index_B
  B.clear()
  random = randint(0,49)
  while (index_A == random):
    random = randint(0,49)
  index_B = random
  
  for i in data[index_B]:
    B.append(data[index_B][i])
  
  return B
# create check answer function
def check(option):
  global A
  global B
  global score
  if option == 'A':
     if A[1] > B[1]:
       score +=1
       return True
     else:
       return False

  if option == 'B':
     if B[1] > A[1]:
       A=B
       score +=1
       return True
     else:
       return False     


#initial runtime
A = compare_a()
print(f"Compare A : {A[0]}, a {A[2]}, from {A[3]}")
# SHOW VS
print(vs)

B = compare_b()
print(f"Compare B : {B[0]}, a {B[2]}, from {B[3]}")

# PRINT ASK
option = input("Who has more followers? Type 'A' or 'B': ")

# CALL CHECK ANSWER
result = check(option)
 
# START THE WHILE LOOP
while(result):
  os.system("clear")  
  # SHOW GRAPHICS
  print(logo)
  # SHOW SCORE
  print(f"You are right, the current score is {score}")
# CHOOSE ANSWER
  print(f"Compare A : {A[0]}, a {A[2]}, from {A[3]}")
# VS
  print(vs)  
# CHOOSE B
  B = compare_b()
  print(f"Compare B : {B[0]}, a {B[2]}, from {B[3]}")

# PRINT ASK
  option = input("Who has more followers? Type 'A' or 'B': ")
# CHECK ANSWER
  result = check(option)
# OUTSIDE WHILE PRINT GAME OVER
print(f"Sorry, that's wrong. Final score: {score}")
