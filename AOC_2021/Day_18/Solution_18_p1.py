import re
import copy
import math

def main():
    math_input = Input_to_List('Day_18/Input_18.txt')
    math_problem = Reduce(math_input[0], math_input[1])
    if len(math_input) > 2:
        for line in math_input[2:]:
            math_problem = Reduce([math_problem,line])
    print(math_problem)
    magnitude = Get_Magnitude(math_problem)
    print(magnitude)

    
def Input_to_List(path):

    # match_string = r"\d"

    file = open(path, 'r')
    line = file.readline().strip()
    # row = list(map(int,re.findall(match_string, line)))

    return_list = []

    while True:
        if not line:
            break
        else:
            return_list.append(line)
            line = file.readline().strip()
            # row = list(map(int,re.findall(match_string, line)))
            
    return return_list

# Passes number to appropriate functions
def Reduce(terms):
    # Finds all strings where two terms are immediately present (don't have to wait for other explode or split operations)
    search_string = r"\[\d+,\d+\]"
    pass

# If the term is nested inside 4 other pairs of brackets
# [[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4]
def Explode(start_location, end_location, expression, term):
    no_term_left = False
    no_term_right = False
    length = len(expression)
    left_location = start_location - 1
    right_location = end_location
    left_num = expression[left_location]
    right_num = expression[right_location]

    while (not left_num.isdigit() and left_location >= 0):
        left_location -= 1
        left_num = expression[left_location]

    left_location -= 1
    while (expression[left_location].isdigit() and left_location >= 0):
        left_num.append(expression[left_location])
        left_location -= 1

    if left_num.isdigit():
        left_num = left_num[::-1]
    else:
        no_term_left = True
    


    while (not right_num.isdigit() and right_location < length):
        right_location += 1
        right_num = expression[right_location]

    right_location += 1
    while (expression[right_location].isdigit() and right_location < length):
        right_num.append(expression[right_location])
        right_location += 1

    if not right_num.isdigit():
        no_term_right = True



#If the term is >= 10
# 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6]
def Split(term):
    base = float(term) / 2
    left = math.floor(base)
    right = math.ceil(base)

    return f"[{left},{right}]"




# 3x the left term + 2x the right term
def Get_Magnitude(math_problem):
    pass


if __name__ == '__main__':
    main()

