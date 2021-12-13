import re

def main():
    cave_list = Input_to_List('Day_9/Input_9.txt')
    basins = Find_Basins(cave_list)
    basin_total = Basin_Multiply(basins)
    print(basin_total)    

def Input_to_List(path):
    #Gets all numbers in the line and puts them in a list as strings
    match_string = r"\d"

    file = open(path, 'r')
    line = file.readline()
    numbers = re.findall(match_string, line)
    integers = [int(number) for number in numbers]

    return_list = []

    while True:
        if not line:
            break
        else:
            return_list.append(integers)
            line = file.readline().strip()
            numbers = re.findall(match_string, line)
            integers = [int(number) for number in numbers]            

    return return_list


def Find_Basins(cave_list):
    basin_coordinates = []

    #start with a basin. Go row by row and term by term, adding each vent to the basin it's touching
    #if a vent is touching two basins, combine the basins into one
    #Will need to track indicies to determine if it's touching a basin
    for row_index,row in enumerate(cave_list):
        for height_index,height in enumerate(row):
            if height < 9:
                #only need to check up and left, since those will be the only processed numbers available
                basin_up = None
                basin_left = None

                for basin_index,basin in enumerate(basin_coordinates):
                    if (row_index > 0) and ([row_index-1,height_index] in basin):
                        basin_up = basin_index
                    if (height_index > 0) and ([row_index,height_index-1] in basin):
                        basin_left = basin_index

                if basin_up != None:
                    if basin_left == None or basin_left == basin_up:
                        basin_coordinates[basin_up].append([row_index,height_index])
                    else:
                        for coordinate in basin_coordinates[basin_left]:
                            basin_coordinates[basin_up].append(coordinate)                        
                        basin_coordinates[basin_up].append([row_index,height_index])
                        basin_coordinates.pop(basin_left)
                elif basin_left != None:
                    basin_coordinates[basin_left].append([row_index,height_index])
                else:
                    basin_coordinates.append([[row_index,height_index]])

    return basin_coordinates


def Basin_Multiply(basins):
    first = 0
    second = 0
    third = 0

    for basin in basins:
        if len(basin) >= first:
            third = second
            second = first
            first = len(basin)
        elif len(basin) >= second:
            third = second
            second = len(basin)
        elif len(basin) > third:
            third = len(basin)

    return first * second * third


if __name__ == '__main__':
    main()