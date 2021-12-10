import re

def main():
    input_list = Input_to_List('Day_10/Input_10.txt')
    corrupt_chars = Corrupt_Lines(input_list)
    total = Score(corrupt_chars)
    print(total)



def Input_to_List(path):
    file = open(path, 'r')
    line = file.readline().strip()

    return_list = []

    while True:
        if not line:
            break
        else:
            return_list.append(line)
            line = file.readline().strip()

    return return_list


def Corrupt_Lines(input_list):
    pair_dict = {'(':')', '[':']', '{':'}', '<':'>'}
    openers = ['(', '[', '{', '<']

    corrupt_characters = []
    
    for line in input_list:
        stack = []
        for character in line:
            if stack == [] and character in openers:
                stack.append(character)
            elif character == pair_dict[stack[len(stack)-1]]:
                stack.pop()
            elif character in openers:
                stack.append(character)
            else:
                corrupt_characters.append(character)
                break

    return corrupt_characters



def Score(corrupt_lines):
    score_dict = {')':3, ']':57, '}':1197, '>':25137}
    total = 0

    for line in corrupt_lines:
        total += score_dict[line]

    return total


if __name__ == '__main__':
    main()