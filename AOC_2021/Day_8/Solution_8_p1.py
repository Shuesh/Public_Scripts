import re

def Main():
    display_list = Input_to_List('Day_8/Input_8.txt')
    alphabetized_list = Alphabetize_Strings(display_list)
    total = Count_Digits(alphabetized_list)
    print(total)
    # display_map = Decode(alphabetized_list)



def Input_to_List(path):
    #Gets all numbers in the line and puts them in a list as strings
    match_string = r"\w+"

    file = open(path, 'r')
    line = file.readline()

    display = []

    while True:
        if not line:
            break
        else:
            display_digits = re.findall(match_string, line)
            display.append(display_digits)
            line = file.readline()

    return display


def Alphabetize_Strings(display_list):
    alphabetized_strings = []

    for line in display_list:
        line_digits = []
        for digit in line:
            alphabetized_digits = sorted(digit)
            alphabetized_string = ''.join(alphabetized_digits)
            line_digits.append(alphabetized_string)
        alphabetized_strings.append(line_digits)

    return alphabetized_strings



def Decode(alphabetized_list):
    display_map = {'a':['a','b','c','d','e','f','g'], 'b':['a','b','c','d','e','f','g'], 'c':['a','b','c','d','e','f','g'], 'd':['a','b','c','d','e','f','g'], 'e':['a','b','c','d','e','f','g'], 'f':['a','b','c','d','e','f','g'], 'g':['a','b','c','d','e','f','g']}

    for line in alphabetized_list:
        ordered_digits = [None for _ in range(14)]
        for digit in line:
            if len(digit) == 2:
                ordered_digits[1] = digit
                display_map[digit[0]]
            elif len(digit) == 4:
                ordered_digits[4] = digit
            elif len(digit) == 3:
                ordered_digits[7] = digit
            elif len(digit) == 7:
                ordered_digits[8] = digit



def Count_Digits(alphabetized_list):
    count = 0

    for line in alphabetized_list:
        for index in range(10,14):
            if len(line[index]) == 2:
                count += 1
            elif len(line[index]) == 4:
                count += 1
            elif len(line[index]) == 3:
                count += 1
            elif len(line[index]) == 7:
                count += 1

    return count



if __name__ == '__main__':
    Main()