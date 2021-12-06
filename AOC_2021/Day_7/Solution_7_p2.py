import re

def main():
    input_list = Input_to_List('Day_7/Example_7.txt')
    


def Input_to_List(path):
    #Gets all numbers in the line and puts them in a list as strings
    match_string = r"\d+"

    file = open(path, 'r')
    line = file.readline()
    numbers = re.findall(match_string, line)

    return_list = []

    while True:
        if not line:
            break
        else:
            return_list.append(line.strip())
            line = file.readline()

    return return_list




def Function():
    pass




if __name__ == '__main__':
    main()