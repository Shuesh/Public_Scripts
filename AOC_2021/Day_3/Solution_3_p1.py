def main():
    instruction_list = Input_to_List('Day_3/Example_3.txt')

    print()


def Input_to_List(path):
    file = open(path, 'r')
    line = file.readline()

    return_list = []

    while (line != ''):
        return_list.append(line.strip())
        line = file.readline()

    return return_list

def Function():
    pass


if __name__ == '__main__':
    main()