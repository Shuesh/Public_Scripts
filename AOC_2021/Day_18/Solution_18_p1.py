import re
import copy


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


def Reduce(terms):
    pass


def Explode(pair):
    pass


def Split(pair):
    pass


def Get_Magnitude(math_problem):
    pass


if __name__ == '__main__':
    main()

