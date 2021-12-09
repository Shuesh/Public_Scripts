import re

def main():
    cave_list = Input_to_List('Day_9/Input_9.txt')
    lows = Find_Lows(cave_list)
    risk_total = Risk_Levels(lows)
    print(risk_total)    


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




def Find_Lows(cave_list):
    num_rows = len(cave_list)
    row_length = len(cave_list[0])
    lows = []
    lows_indicies = []

    for row_index,row in enumerate(cave_list):
        for term_index,term in enumerate(row):
            if row_index > 0:
                if cave_list[row_index-1][term_index] <= term:
                    continue
            if row_index < num_rows-1:
                if cave_list[row_index+1][term_index] <= term:
                    continue
            if term_index > 0:
                if cave_list[row_index][term_index-1] <= term:
                    continue
            if term_index < row_length-1:
                if cave_list[row_index][term_index+1] <= term:
                    continue
            lows.append(term)
            lows_indicies.append([row_index,term_index])
    
    return lows
            

def Risk_Levels(lows):
    total = 0

    for low in lows:
        total += low+1

    return total


if __name__ == '__main__':
    main()