
def solution(map):
    path_finder(map, 0, 0, 0, len(map), len(map[0]), 0))

def path_finder(map):
    map_height = len(map) - 1
    map_width = len(map[0]) - 1
    walls_removed = 0
    index_x = 0
    index_y = 0
    path_length = 0
    came_from = 'up'

    while (index_x < map_width or index_y < map_height):
        movement = direction(map, index_y, index_x, walls_removed, came_from)




def direction(map, position_y, position_x, walls_removed, came_from):
    #order goes down, right, left, up
    step1_array = []
    #order goes SE, S, E, SW, NE, W, N, NW
    step2_array = []

    




# . . 2 . .
# . 2 1 2 .
# 2 1 X 1 2
# . 2 1 2 .
# . . 2 . .




#Height and width from 2-20

#Start
# 0 1 1 0
# 0 0 0 1
# 1 1 0 0
# 1 1 1 0
#       Finish
# Answer: 7


#Start
# 0 0 0 0 0 0
# 1 1 1 1 1 0
# 0 0 0 0 0 0
# 0 1 1 1 1 1
# 0 1 1 1 1 1
# 0 0 0 0 0 0
#           Finish
# Answer: 11



def recursive_path_finder(map, location_x, location_y, walls, height, width, path_length):

    #End condition (Success and Failure)
    if (location_x == width-1 and location_y == height-1 and walls >= 1):
        print(path_length)

    #Move Down
    if (location_y < height-1):
        if(map[location_y][location_x] == 0):
            recursive_path_finder(map, location_x, location_y+1, walls, height, width, path_length+1)
    if (location_x < width-1):
        if(map[location_y][location_x] == 0):
            recursive_path_finder(map, location_x+1, location_y, walls, height, width, path_length+1)

    if (location_y < height-1):
        if(map[location_y][location_x] == 1 and walls == 0):
            recursive_path_finder(map, location_x, location_y+1, walls+1, height, width, path_length+1)
    if (location_x < width-1):
        if(map[location_y][location_x] == 1 and walls == 0):
            recursive_path_finder(map, location_x+1, location_y, walls+1, height, width, path_length+1)


    #Move Left
    if (location_x > 1):
        if(map[location_y][location_x] == 0):
            recursive_path_finder(map, location_x-1, location_y, walls, height, width, path_length+1)
        elif(map[location_y][location_x] == 1 and walls == 0):
            recursive_path_finder(map, location_x-1, location_y, walls+1, height, width), path_length+1


    #Move Up
    if (location_y > 1):
        if(map[location_y][location_x] == 0):
            recursive_path_finder(map, location_x, location_y-1, walls, height, width, path_length+1)
        if(map[location_y][location_x] == 1 and walls == 0):
            recursive_path_finder(map, location_x, location_y-1, walls+1, height, width, path_length+1)

solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])

