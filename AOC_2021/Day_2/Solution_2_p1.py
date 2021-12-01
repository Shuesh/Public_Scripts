def main():
    elevation_list = Input_to_List('Day_1/Input_1.txt')
    print()


def Input_to_List(path):
    file = open(path, 'r')
    line = file.readline()

    return_list = []

    while (line != ''):
        return_list.append(int(line.strip()))
        line = file.readline()

    return return_list




if __name__ == '__main__':
    main()