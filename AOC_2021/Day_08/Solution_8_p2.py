import re

def Main():
    display_list = Input_to_List('Day_8/Input_8.txt')
    alphabetized_list = Alphabetize_Strings(display_list)
    ordered_list = Order(alphabetized_list)
    decoded_integers = Decode(ordered_list)
    total = Sum_Numbers(decoded_integers)
    print(total)



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


def Order(alphabetized_list):
    decoded_lines = []

    for line in alphabetized_list:
        ordered_digits = [None for _ in range(10)]
        while True:
            if None in ordered_digits:
                for digit in line[:10]:
                    # 1
                    if ordered_digits[1] == None and len(digit) == 2:
                        ordered_digits[1] = digit
                    # 7
                    elif ordered_digits[7] == None and len(digit) == 3:
                        ordered_digits[7] = digit
                    # 4
                    elif ordered_digits[4] == None and len(digit) == 4:
                        ordered_digits[4] = digit
                    # 2, 3, 5
                    elif len(digit) == 5 and (ordered_digits[1] != None and ordered_digits[9] != None) and \
                        (ordered_digits[2] == None or ordered_digits[3] == None or ordered_digits[5] == None):

                        if ((ordered_digits[1][0] in digit) and (ordered_digits[1][1] in digit)):
                            ordered_digits[3] = digit
                        elif ((digit[0] in ordered_digits[9]) and (digit[1] in ordered_digits[9]) and \
                            (digit[2] in ordered_digits[9]) and (digit[3] in ordered_digits[9]) and (digit[4] in ordered_digits[9])):

                            ordered_digits[5] = digit
                        else:
                            ordered_digits[2] = digit
                    # 0, 6, 9
                    elif len(digit) == 6 and (ordered_digits[4] != None) and (ordered_digits[7] != None):
                        if (ordered_digits[4][0] in digit) and (ordered_digits[4][1] in digit) and (ordered_digits[4][2] in digit) and (ordered_digits[4][3] in digit):
                            ordered_digits[9] = digit
                        elif (ordered_digits[7][0] in digit) and (ordered_digits[7][1]in digit) and (ordered_digits[7][2] in digit):
                            ordered_digits[0] = digit
                        else: 
                            ordered_digits[6] = digit
                    # 8
                    elif ordered_digits[8] == None and len(digit) == 7:
                        ordered_digits[8] = digit
            else:
                for i in line[10:]:
                    ordered_digits.append(i)
                decoded_lines.append(ordered_digits)
                break

    return decoded_lines


def Decode(ordered_list):
    decoded_integers = []

    for line in ordered_list:
        display_number = ''
        for number in line[10:]:               
            display_number = display_number + str(line.index(number))
        
        decoded_integers.append(display_number)

    return decoded_integers


def Sum_Numbers(decoded_numbers):
    total = 0

    for number in decoded_numbers:
        total += int(number)

    return total



if __name__ == '__main__':
    Main()