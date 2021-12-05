import re

def main():
    max_size = 1000

    input_list = Input_to_List('Day_6/Example_6.txt')
    vent_map = [[0 for _ in range(max_size)] for _ in range(max_size)]
    vent_map = Draw_Lines(input_list, vent_map)
    count = Count_Overlaps(vent_map)
    print(count)


def Input_to_List(path):
    match_string = r"\d+"

    file = open(path, 'r')

    return_list = []

    while True:
        line = file.readline().strip()
        coordinates = re.findall(match_string, line)

        if not line:
            break
        else:
            return_list.append([int(coordinates[0]),int(coordinates[1]),int(coordinates[2]),int(coordinates[3])])

    return return_list

def Draw_Lines(input_list, vent_map):

    for line in input_list:
        direction = None
        if (line[0] == line[2]):
            minimum = min(line[1],line[3])
            maximum = max(line[1],line[3])
            direction = 'vertical'
        elif (line[1] == line[3]):
            minimum = min(line[0],line[2])
            maximum = max(line[0],line[2])
            direction = 'horizontal'
        
        for index in range(minimum,maximum+1):
            if direction == 'horizontal':
                vent_map[line[1]][index] += 1
            elif direction == 'vertical':
                vent_map[index][line[0]] += 1
    
    return vent_map


def Count_Overlaps(vent_map):
    count = 0

    for row in vent_map:
        for term in row:
            if (term >= 2):
                count += 1

    return count


if __name__ == '__main__':
    main()