def main():
    instruction_list = Input_to_List('Day_2/Input_2.txt')
    depth, h_pos = Change_Position(instruction_list)
    print(depth * h_pos)


def Input_to_List(path):
    file = open(path, 'r')
    line = file.readline()

    return_list = []

    while (line != ''):
        return_list.append(line.strip())
        line = file.readline()

    return return_list


def Change_Position(instruction_list):
    aim = 0
    depth = 0
    h_pos = 0

    for instruction in instruction_list:
        if (instruction[0] == 'f'):
            h_pos += int(instruction[-1])
            depth += aim * int(instruction[-1])
        elif (instruction[0] == 'u'):
            aim -= int(instruction[-1])
        elif (instruction[0] == 'd'):
            aim += int(instruction[-1])


    return depth, h_pos


if __name__ == '__main__':
    main()