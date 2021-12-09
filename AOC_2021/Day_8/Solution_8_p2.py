import re

def main():
    cave_list = Input_to_List('Day_8/Input_8.txt')
    nines = Find_Nines(cave_list)
    basins = Find_Basins(cave_list, nines)
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


def Find_Nines(cave_list):
    nines = []

    for row_index,row in enumerate(cave_list):
        for vent_index,vent in enumerate(row):
            if vent == 9:
                nines.append([row_index,vent_index])

    return nines


def Find_Basins(cave_list, nines):
    basin_extents = []

    #start with a basin. Go row by row and term by term, adding each vent to the basin it's touching
    #if a vent is touching two basins, combine the basins into one
    #Will need to track indicies to determine if it's touching a basin
     
            

def Basin_Multiply(basins):
    first = 0
    second = 0
    third = 0

    for basin in basins:
        if len(basin) >= first:
            third = second
            second = first
            first = len(basin)

    return first * second * third


if __name__ == '__main__':
    main()