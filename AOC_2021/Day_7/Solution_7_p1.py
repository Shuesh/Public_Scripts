import re

def Main():
    crab_list = Input_to_List('Day_7/Input_7.txt')
    
    #this is a dictionary
    crab_quantities = Quantitizer(crab_list)
    mode = max(crab_quantities, key=crab_quantities.get)
    mean = Find_Mean(crab_quantities)
    total = Gas_Expenditure(crab_quantities, mode)
    print(total)

    


def Input_to_List(path):
    #Gets all numbers in the line and puts them in a list as strings
    match_string = r"\d+"

    file = open(path, 'r')
    line = file.readline()
    numbers = re.findall(match_string, line)

    integers = [int(number) for number in numbers]

    return integers


def Quantitizer(crab_list):
    crab_quantities = dict()

    for crab in crab_list:
        if crab not in crab_quantities:
            crab_quantities[crab] = 1
        else:
            crab_quantities[crab] += 1

    return crab_quantities

def Find_Mean(crab_quantities):
    length = 0
    total = 0

    for crab in crab_quantities:
        length += crab_quantities[crab]
        total += crab * crab_quantities[crab]

    return total/length

def Gas_Expenditure(crab_quantities, mode):
    total = 0

    for crab in crab_quantities:
        total += crab_quantities[crab] * abs(crab-mode)

    return total


if __name__ == '__main__':
    Main()