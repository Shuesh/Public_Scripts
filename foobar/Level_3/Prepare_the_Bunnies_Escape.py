import copy

def solution(map):
    height = len(map)
    width = len(map[0])
    map_copy = copy.deepcopy(map)
    min_path_length = 9999999
    empty_array = initialize_array(height,width)
    path_length = dijkstras_path_finder(map_copy, empty_array, height-1, width-1)
    if (path_length != None):
        min_path_length = path_length
    for row in range(len(map)):
        for column in range(len(map[0])):
            if (min_path_length != None and min_path_length == height + width + 1):
                break
            if map[row][column] == 1:
                map_copy = copy.deepcopy(map)
                map_copy[row][column] = 0
                empty_array = initialize_array(height,width)
                path_length = dijkstras_path_finder(map_copy, empty_array, height-1, width-1)
                if (path_length != None and path_length < min_path_length):
                    min_path_length = path_length

    print(min_path_length)

def initialize_array(height, width):
    empty_array = [[['X',False] for i in range(width)] for j in range(height)]
    return empty_array
    

def dijkstras_path_finder(map, dijkstra_array, location_y, location_x):
    queue = []
    dijkstra_array[location_y][location_x][1] = True
    dijkstra_array[location_y][location_x][0] = 1
    queue.append([location_y,location_x])
    while queue:
        location = queue.pop(0)
        if location == [0,0]:
            return dijkstra_array[0][0][0]
        #Check the location above
        if location[0] > 0 and dijkstra_array[location[0]-1][location[1]][1] == False:
            dijkstra_array[location[0]-1][location[1]][1] = True
            if map[location[0]-1][location[1]] == 0:
                queue.append([location[0]-1,location[1]])
                if location[1] < len(map[0])-1 and dijkstra_array[location[0]-1][location[1]+1][0] != 'X':
                    right = dijkstra_array[location[0]-1][location[1]+1][0]
                else:
                    right = 9999999
                if location[0] <= len(map)-1 and dijkstra_array[location[0]][location[1]][0] != 'X':
                    down = dijkstra_array[location[0]][location[1]][0]
                else:
                    down = 9999999
                if location[0] > 1 and dijkstra_array[location[0]-2][location[1]][0] != 'X':
                    up = dijkstra_array[location[0]-2][location[1]][0]
                else:
                    up = 9999999
                if location[1] > 0 and dijkstra_array[location[0]-1][location[1]-1][0] != 'X':
                    left = dijkstra_array[location[0]-1][location[1]-1][0]
                else: 
                    left = 9999999
                minimum_path = min(right,down,up,left)
                dijkstra_array[location[0]-1][location[1]][0] = minimum_path + 1
        #Check the location to the left
        if location[1] > 0 and dijkstra_array[location[0]][location[1]-1][1] == False:
            dijkstra_array[location[0]][location[1]-1][1] = True
            if map[location[0]][location[1]-1] == 0:
                queue.append([location[0],location[1]-1])
                if location[1] <= len(map[0])-1 and dijkstra_array[location[0]][location[1]][0] != 'X':
                    right = dijkstra_array[location[0]][location[1]][0]
                else:
                    right = 9999999
                if location[0] < len(map)-1 and dijkstra_array[location[0]+1][location[1]-1][0] != 'X':
                    down = dijkstra_array[location[0]+1][location[1]-1][0]
                else:
                    down = 9999999
                if location[0] > 0 and dijkstra_array[location[0]-1][location[1]-1][0] != 'X':
                    up = dijkstra_array[location[0]-1][location[1]-1][0]
                else:
                    up = 9999999
                if location[1] > 1 and dijkstra_array[location[0]][location[1]-2][0] != 'X':
                    left = dijkstra_array[location[0]][location[1]-2][0]
                else: 
                    left = 9999999
                minimum_path = min(right,down,up,left)
                dijkstra_array[location[0]][location[1]-1][0] = minimum_path + 1
        #Check the location below
        if location[0] < len(map)-1 and dijkstra_array[location[0]+1][location[1]][1] == False:
            dijkstra_array[location[0]+1][location[1]][1] = True
            if map[location[0]+1][location[1]] == 0:
                queue.append([location[0]+1,location[1]])
                if location[1] < len(map[0])-1 and dijkstra_array[location[0]+1][location[1]+1][0] != 'X':
                    right = dijkstra_array[location[0]+1][location[1]+1][0]
                else:
                    right = 9999999
                if location[0] < len(map)-3 and dijkstra_array[location[0]+2][location[1]][0] != 'X':
                    down = dijkstra_array[location[0]+2][location[1]][0]
                else:
                    down = 9999999
                if location[0] < len(map)-1 and dijkstra_array[location[0]][location[1]][0] != 'X':
                    up = dijkstra_array[location[0]][location[1]][0]
                else:
                    up = 9999999
                if location[1] > 0 and dijkstra_array[location[0]+1][location[1]-1][0] != 'X':
                    left = dijkstra_array[location[0]+1][location[1]-1][0]
                else: 
                    left = 9999999
                minimum_path = min(right,down,up,left)
                dijkstra_array[location[0]+1][location[1]][0] = minimum_path + 1
        #Check the location to the right
        if location[1] < len(map[0])-1 and dijkstra_array[location[0]][location[1]+1][1] == False:
            dijkstra_array[location[0]][location[1]+1][1] = True
            if map[location[0]][location[1]+1] == 0:
                queue.append([location[0],location[1]+1])
                if location[1] <= len(map[0])-3 and dijkstra_array[location[0]][location[1]+2][0] != 'X':
                    right = dijkstra_array[location[0]][location[1]+2][0]
                else:
                    right = 9999999
                if location[0] < len(map)-2 and dijkstra_array[location[0]+1][location[1]+1][0] != 'X':
                    down = dijkstra_array[location[0]+1][location[1]+1][0]
                else:
                    down = 9999999
                if location[0] > 0 and dijkstra_array[location[0]-1][location[1]+1][0] != 'X':
                    up = dijkstra_array[location[0]-1][location[1]+1][0]
                else:
                    up = 9999999
                if location[1] >= 0 and dijkstra_array[location[0]][location[1]][0] != 'X':
                    left = dijkstra_array[location[0]][location[1]][0]
                else: 
                    left = 9999999
                minimum_path = min(right,down,up,left)
                dijkstra_array[location[0]][location[1]+1][0] = minimum_path + 1


# solution([
#     [0,1,1,0],
#     [0,0,0,1],
#     [1,1,0,0],
#     [1,1,1,0]
# ])
# Answer: 7


# solution([
#     [0,0,0,0,0,0],
#     [1,1,1,1,1,0],
#     [0,0,0,0,0,0],
#     [0,1,1,1,1,1],
#     [0,1,1,1,1,1],
#     [0,0,0,0,0,0]
# ])
# Answer: 11

solution([
    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
    [0,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0],
    [0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0],
    [0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0],
    [0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0],
    [0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0],
    [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0],
    [0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0],
    [0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,0,1,0],
    [0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0],
    [0,1,0,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0],
    [0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0],
    [0,1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0],
    [0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0],
    [0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0]
])
# Answer: 66

# solution([
#     [0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
#     [0,1,0,1,1,0,1,0,1,0,0,0,1,0,0,0],
#     [0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1],
#     [0,1,0,0,0,0,1,1,0,0,1,0,0,0,1,0],
#     [1,1,1,1,0,1,1,0,0,1,0,0,0,1,0,0],
#     [0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0],
#     [0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0],
#     [0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0],
#     [1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
#     [0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1],
#     [0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
#     [0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
#     [0,1,0,0,1,1,0,0,1,1,1,1,1,0,1,1],
#     [0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0],
#     [0,0,1,0,0,0,0,0,1,0,1,0,1,1,1,1],
#     [0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
#     [1,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1],
#     [0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0],
#     [0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]
# ])
# Answer: 47

# solution([
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# ])
# Answer: 31