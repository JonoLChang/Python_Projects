#import sys

#while True:
#    print('Type exit to exit.')
 #   response = input()
  #  if response == 'exit':
   #     sys.exit()
    #print('You typed ' + response + '.')

#for i in ['J', 'K', 'L', 'O']:
 #   print(i)

import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nextCells.append(column) # nextCells is a list of column lists.

print(nextCells)