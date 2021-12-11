import re

def main():
    input_list = Input_to_List('Day_12/Example_12.txt')




def Input_to_List(path):
    file = open(path, 'r')
    line = list(file.readline().strip())
    octopus_line = []
    for octopus in line:
        octopus_line.append(int(octopus))

    return_list = []

    while True:
        if not line:
            break
        else:
            return_list.append(octopus_line)
            line = list(file.readline().strip())
            octopus_line = []
            for octopus in line:
                octopus_line.append(int(octopus))

    return return_list




if __name__ == '__main__':
    main()