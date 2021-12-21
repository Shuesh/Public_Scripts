import re
import copy


def main():
    chiton_grid = Input_to_List('Day_15/Input_15.txt')
    expanded_grid = Expand_Map(chiton_grid)
    length = Width_Recursive_Search(expanded_grid)
    print(length)
    


def Input_to_List(path):

    match_string = r"\d"

    file = open(path, 'r')
    line = file.readline().strip()
    row = list(map(int,re.findall(match_string, line)))

    return_list = []


    while True:
        if not line:
            break
        else:
            return_list.append(row)
            line = file.readline().strip()
            row = list(map(int,re.findall(match_string, line)))
            
    return return_list


def Expand_Map(chiton_grid):
    expanded_grid = []

    for i in range(5):
        for row_idx, row in enumerate(chiton_grid):
            expanded_row = []
            for j in range(5):
                for term in row:
                    number = term + i + j
                    if number > 9:
                        number -= 9
                    expanded_row.append(number)
            expanded_grid.append(expanded_row)

    return expanded_grid



def Width_Recursive_Search (chiton_grid):

    distance_grid = [[None for _ in range(len(chiton_grid[0]))] for __ in range(len(chiton_grid))]
    distance_grid[0][0] = 0

    queue = [[0,0]]

    while queue:
        coordinate = queue.pop(0)
        #up
        if coordinate[0] > 0:
            up_length = distance_grid[coordinate[0]][coordinate[1]] + chiton_grid[coordinate[0]-1][coordinate[1]]
            if distance_grid[coordinate[0]-1][coordinate[1]] == None or up_length < distance_grid[coordinate[0]-1][coordinate[1]]:
                distance_grid[coordinate[0]-1][coordinate[1]] = up_length
                queue.append([coordinate[0]-1,coordinate[1]])
        #down
        if coordinate[0] < len(chiton_grid)-1:
            down_length = distance_grid[coordinate[0]][coordinate[1]] + chiton_grid[coordinate[0]+1][coordinate[1]]
            if distance_grid[coordinate[0]+1][coordinate[1]] == None or down_length < distance_grid[coordinate[0]+1][coordinate[1]]:
                distance_grid[coordinate[0]+1][coordinate[1]] = down_length
                queue.append([coordinate[0]+1,coordinate[1]])
        #left
        if coordinate[1] > 0:
            left_length = distance_grid[coordinate[0]][coordinate[1]] + chiton_grid[coordinate[0]][coordinate[1]-1]
            if distance_grid[coordinate[0]][coordinate[1]-1] == None or left_length < distance_grid[coordinate[0]][coordinate[1]-1]:
                distance_grid[coordinate[0]][coordinate[1]-1] = left_length
                queue.append([coordinate[0],coordinate[1]-1])
        #right
        if coordinate[1] < len(chiton_grid[0])-1:
            right_length = distance_grid[coordinate[0]][coordinate[1]] + chiton_grid[coordinate[0]][coordinate[1]+1]
            if distance_grid[coordinate[0]][coordinate[1]+1] == None or right_length < distance_grid[coordinate[0]][coordinate[1]+1]:
                distance_grid[coordinate[0]][coordinate[1]+1] = right_length
                queue.append([coordinate[0],coordinate[1]+1])

    return distance_grid[len(chiton_grid)-1][len(chiton_grid[0])-1]


if __name__ == '__main__':
    main()




