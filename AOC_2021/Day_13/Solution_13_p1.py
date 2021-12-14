import re
import copy


def main():
    coordinate_list, fold_list = Input_to_List('Day_13/Input_13.txt')
    coordinate_map = Coordinate_Map(coordinate_list)
    if fold_list[0][0] == 'x':
        coordinate_map = Fold_Horizontal(coordinate_map, fold_list[0][1])
    elif fold_list[0][0] == 'y':
        coordinate_map = Fold_Vertical(coordinate_map, fold_list[0][1])
    total = Count_Dots(coordinate_map)
    print(total)



def Input_to_List(path):
    #Gets all caves
    match_string = r"\d+"

    file = open(path, 'r')
    line = file.readline()
    coordinate = re.findall(match_string, line)

    coordinate_list = []

    while True:
        if not line.strip():
            break
        else:
            coordinate_list.append([int(coordinate[0]), int(coordinate[1])])

            line = file.readline()
            coordinate = re.findall(match_string, line)

    
    line = file.readline()
    fold_list = []

    while True:
        if not line:
            break
        else:
            fold_list.append([line[11],int(line[13:].strip())])
            line = file.readline()

    return coordinate_list, fold_list


def Find_Max_Coordinates(coordinate_list):
    max_x = 0
    max_y = 0

    for coordinate in coordinate_list:
        if coordinate[0] > max_x:
            max_x = coordinate[0]
        if coordinate[1] > max_y:
            max_y = coordinate[1]

    return max_x, max_y


def Coordinate_Map(coordinate_list):
    max_x, max_y = Find_Max_Coordinates(coordinate_list)

    #Initialize with no dots
    coordinate_map = [['.' for _ in range(max_x+1)] for __ in range(max_y+1)]
    
    for coordinate in coordinate_list:
        coordinate_map[coordinate[1]][coordinate[0]] = '#'

    return coordinate_map



#For when the crease runs horizontally (the fold direction is vertical)
def Fold_Vertical(coordinate_map, fold_line):

    #excludes the fold line
    new_list = copy.deepcopy(coordinate_map[:fold_line])

    for row_index,row in enumerate(coordinate_map[fold_line+1:]):
        for spot_index,spot in enumerate(row):
            if new_list[fold_line-1-row_index][spot_index] == '#' or spot == '#':
                new_list[fold_line-1-row_index][spot_index] = '#'

    return new_list


#For when the crease runs vertically (the fold direction is horizontal)
def Fold_Horizontal(coordinate_map, fold_line):
    new_list = [['.' for _ in range(len(coordinate_map[:][:fold_line]))] for __ in range(len(coordinate_map))]

    for index_row_n, row_n in enumerate(new_list):
        for index_spot_n, spot_n in enumerate(row_n):
            new_list[index_row_n][index_spot_n] = coordinate_map[index_row_n][index_spot_n]

    for row_index,row in enumerate(coordinate_map):
        temp = row[fold_line+1:]
        for spot_index,spot in enumerate(row[fold_line+1:]):
            if new_list[row_index][fold_line-1-spot_index] == '#' or spot == '#':
                new_list[row_index][fold_line-1-spot_index] = '#'

    return new_list

    

def Count_Dots(coordinate_map):
    total = 0

    for line in coordinate_map:
        for spot in line:
            if spot == '#':
                total += 1

    return total


if __name__ == '__main__':
    main()