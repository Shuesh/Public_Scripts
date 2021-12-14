def main():
    elevation_list = Input_to_List('Day_1/Input_1.txt')
    print(Number_Increases(elevation_list))


def Input_to_List(path):
    file = open(path, 'r')
    line = file.readline()

    return_list = []

    while (line != ''):
        return_list.append(int(line.strip()))
        line = file.readline()

    return return_list


def Number_Increases(elevation_list):
    count = 0
    prev_elevation = elevation_list[0]

    for elevation in elevation_list:
        if (elevation > prev_elevation):
            count += 1
        prev_elevation = elevation

    return count



if __name__ == '__main__':
    main()