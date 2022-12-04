import pandas as pd
import requests
A = 'Rock'
B = 'Paper'
C = 'Scissor'

X = 1 #rock
Y = 2 #paper
Z = 3 #scissor

win = 6
draw = 3
lose = 0

score = 0
test = 'sample.txt'
data = 'data.txt'
#open the data
with open(data) as file:
    file_contents = file.read()
# split each line of data
    game = file_contents.split('\n')
    for i in game:
      shapes = i.split(' ')
      them = shapes[0]
      me = shapes[1]
      # they play Rock
      if them == 'A':
        # i play rock
        if me == 'X':
          score += X + draw
        # I play paper
        if me == 'Y':
          score += Y + win
        # I play scissor
        if me == 'Z':
          score += Z + lose
      #  they play paper
      elif them == 'B':
        # i play rock
        if me == 'X':
          score += X + lose
        # I play paper
        if me == 'Y':
          score += Y + draw
        # I play scissor
        if me == 'Z':
          score += Z + win
      # they play scissor
      elif them == 'C':
        # I play rock
        if me == 'X':
          score += X + win
        # I play paper
        if me == 'Y':
          score += Y + lose
        # I play scissor
        if me == 'Z':
          score += Z + draw
print(score)

## PART TWO
A = 'Rock'
B = 'Paper'
C = 'Scissor'

win = 6
draw = 3
lose = 0

X = lose
Y = draw
Z = win

rock = 1
paper = 2
scissors = 3

score = 0
test = 'sample.txt'
data = 'data.txt'
#open the data
with open(data) as file:
    file_contents = file.read()

# split each line of data
    game = file_contents.split('\n')
    for i in game:
      shapes = i.split(' ')
      them = shapes[0]
      me = shapes[1]
      # they play Rock
      if them == 'A':
        # i lose
        if me == 'X':
          score += scissors + lose
        # I draw
        if me == 'Y':
          score += rock + draw
        # I win
        if me == 'Z':
          score += paper + win
    
      #  they play paper
      elif them == 'B':
        # i lose
        if me == 'X':
          score += rock + lose
        # I draw
        if me == 'Y':
          score += paper + draw
        # I win
        if me == 'Z':
          score += scissors + win
          
      # they play scissor
      elif them == 'C':
        # i lose
        if me == 'X':
          score += paper + lose
        # I draw
        if me == 'Y':
          score += scissors + draw
        # I win
        if me == 'Z':
          score += rock + win
print(score)
