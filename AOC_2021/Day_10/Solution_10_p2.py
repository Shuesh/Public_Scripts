import re

def main():
    input_list = Input_to_List('Day_10/Input_10.txt')
    corrupt_lines = Corrupt_Lines(input_list)
    for index in reversed(corrupt_lines):
        input_list.pop(index)
    added_chars = Incomplete_Lines(input_list)
    scores_list = Score(added_chars)
    scores_list.sort()
    print(scores_list[len(scores_list)//2])



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
    corrupt_lines = []
    
    for index,line in enumerate(input_list):
        stack = []
        for character in line:
            if stack == [] and character in openers:
                stack.append(character)
            elif character == pair_dict[stack[len(stack)-1]]:
                stack.pop()
            elif character in openers:
                stack.append(character)
            else:
                corrupt_lines.append(index)
                break

    return corrupt_lines



def Incomplete_Lines(input_list):
    pair_dict = {'(':')', '[':']', '{':'}', '<':'>'}
    openers = ['(', '[', '{', '<']
    added_characters = []



    for line in input_list:
        stack = []
        for character in line:
            if stack == [] and character in openers:
                stack.append(character)
            elif character == pair_dict[stack[len(stack)-1]]:
                stack.pop()
            elif character in openers:
                stack.append(character)

        temp = []
        for character in reversed(stack):
            temp.append(pair_dict[character])

        added_characters.append(temp)

    return added_characters


def Score(corrupt_lines):
    score_dict = {')':1, ']':2, '}':3, '>':4}
    scores_list = []
    

    for line in corrupt_lines:
        total = 0
        for character in line:
            total *= 5
            total += score_dict[character]
        scores_list.append(total)

    return scores_list


if __name__ == '__main__':
    main()