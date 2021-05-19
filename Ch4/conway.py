
import random, time, copy
WIDTH = 60
HEIGHT = 20

# generate a random begin sequence
next_cells= [] 
for x in range(WIDTH):
    column = [] # create a column
    for y in range(HEIGHT): 
        if random.randint(0,1) == 0: 
            column.append('#')
        else:
            column.append(' ')
        next_cells.append(column)

# main loop
while True:
    print('\n\n\n\n\n')
    current_cells = copy.deepcopy(next_cells)

# display the cells
    for y in range(HEIGHT):
        for x  in range(WIDTH):
            print(current_cells[x][y], end='')
        print()

    # calculate x and y coordinates
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left_coord = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            # calculate number of neghbors
            num_neighbors = 0
            if current_cells[left_coord][above_coord] == '#': # if top left
                num_neighbors += 1
            if current_cells[x][above_coord] == '#': # if top
                num_neighbors += 1
            if current_cells[right_coord][above_coord] == '#': # if top right
                num_neighbors += 1
            if current_cells[left_coord][y] == '#': # if left
                num_neighbors += 1
            if current_cells[right_coord][y] == '#': # if right
                num_neighbors += 1
            if current_cells[left_coord][below_coord] == '#': # if down left
                num_neighbors += 1
            if current_cells[x][below_coord] == '#': # if down
                num_neighbors += 1
            if current_cells[right_coord][below_coord] == '#': # if down right
                num_neighbors += 1
    
            if current_cells[x][y] == '#' and (num_neighbors == 2 or num_neighbors == 3): # if in the middle and 2 or 3 neighbors
                next_cells[x][y]='#' # will live
            elif current_cells[x][y]=='' and num_neighbors == 3: # if current cell is dead but there are 3 neighbors
                next_cells[x][y]='#' # create a new one
            else:
                next_cells[x][y]='' # die
    time.sleep(1) # zzz for 1 sec ;)


