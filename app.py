import random
import time
import os

# ■
# □
size = 50 # int(input('Enter the world size 20-50 >>>'))
world = [
        list( ' ' for i in range(size) ) for i in range(size)
    ]

# randomize the world
def randomize_the_world(world):
    for (i,w) in enumerate(world):
        for (j,cell) in enumerate(w):
            random_n = random.sample([1,2,3,5,7,8,9,11,13,15,17,19,21,23,25,27,29,31], 1)[0]
            if(random_n % 2 == 0):
                world[i][j] = '■'
    return world

# print the world
def print_the_world(world):
    for w in world:
        for cell in w:
            print( '\033[92m' +cell, end=' ')
        print()

# set the world
def set_the_world(world):
    for (i,w) in enumerate(world):
        for (j,cell) in enumerate(w):
            alive_cell_count = 0


            # top
            try:
                if i-1<0 or i+1>49:
                    raise ZeroDivisionError
                top = world[i-1][j]
                if top == '■':
                    alive_cell_count += 1
            except:
                pass


            # bottom
            try:
                if i-1<0 or i+1>49:
                    raise ZeroDivisionError
                bottom = world[i+1][j]
                if bottom == '■':
                    alive_cell_count += 1
            except:
                pass


            # left
            try:
                if i-1<0 or i+1>49:
                    raise ZeroDivisionError
                left = world[i][j-1]
                if left == '■':
                    alive_cell_count += 1
            except:
                pass


            # right
            try:
                if i-1<0 or i+1>49:
                    raise ZeroDivisionError
                right = world[i][j+1]
                if right == '■':
                    alive_cell_count += 1
            except:
                pass


            # top_left
            try:
                if i-1<0 or i+1>49:
                    raise ZeroDivisionError
                top_left = world[i-1][j-1]
                if top_left == '■':
                    alive_cell_count += 1
            except:
                pass


            # top_right
            try:
                if i-1<0 or i+1>49:
                    raise ZeroDivisionError
                top_right = world[i-1][j+1]
                if top_right == '■':
                    alive_cell_count += 1
            except:
                pass


            # bottom_left
            try:
                if i-1<0 or i+1>49:
                    raise ZeroDivisionError
                bottom_left = world[i+1][j-1]
                if bottom_left == '■':
                    alive_cell_count += 1
            except:
                pass


            # bottom_right
            try:
                if i-1<0 or i+1>49:
                    raise ZeroDivisionError
                bottom_right = world[i+1][j+1]
                if bottom_right == '■':
                    alive_cell_count += 1
            except:
                pass


            # - SET LIFE STATUS -
            # Any live cell with two or three live neighbours survives.
            # Any dead cell with three live neighbours becomes a live cell.
            # All other live cells die in the next generation. Similarly, all other dead cells stay dead.
            if world[i][j] == '■' and ( alive_cell_count == 2 or alive_cell_count == 3 ):
                pass
            elif world[i][j] == ' ' and alive_cell_count == 3:
                world[i][j] = '■'
            elif world[i][j] == '■' and ( alive_cell_count < 2 or alive_cell_count > 3 ):
                world[i][j] = ' '

    return world


# - - -


world = randomize_the_world(world)

while(True):
    print_the_world(world)
    world = set_the_world(world)
    time.sleep(0.5)
    os.system('clear')
