def main():
    elevation_list = Input_to_List('Day_1/Input_1.txt')
    print(Window_Increases(elevation_list))


def Input_to_List(path):
    file = open(path, 'r')
    line = file.readline()

    return_list = []

    while (line != ''):
        return_list.append(int(line.strip()))
        line = file.readline()

    return return_list


def Window_Increases(elevation_list):
    count = 0
    elevation_0 = elevation_list[0]
    elevation_1 = elevation_list[1]
    prev_sum = elevation_0 + elevation_1 + elevation_list[2]

    for elevation in elevation_list[2:]:
        current_sum = elevation_0 + elevation_1 + elevation
        if (current_sum > prev_sum):
            count += 1
        prev_sum = current_sum
        elevation_0 = elevation_1
        elevation_1 = elevation

    return count



if __name__ == '__main__':
    main()