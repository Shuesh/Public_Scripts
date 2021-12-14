import re
import math

def Main():
    crab_list = Input_to_List('Day_7/Example_7.txt')
    
    #this is a dictionary
    crab_quantities = Quantitizer(crab_list)
    mode = max(crab_quantities, key=crab_quantities.get)
    mean = Find_Mean(crab_quantities)
    # median = Find_Median(crab_list)

    total = 100000000000000
    for i in range(min(crab_list),max(crab_list)):
        prev_total = total
        total = Gas_Expenditure(crab_quantities, i)
        if(total > prev_total):
            break
        
    print(prev_total)


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

def Find_Median(crab_list):
    crab_list.sort()

    while (len(crab_list) > 2):
        crab_list.pop(0)
        crab_list.pop(len(crab_list)-1)
    
    if (len(crab_list) == 2):
        median = math.ceil((crab_list[0]+crab_list[1])/2)
    elif (len(crab_list) == 1):
        median = crab_list[0]

    return median


def Gas_Expenditure(crab_quantities, average):
    total = 0
    

    for crab in crab_quantities:
        subtotal = 0
        for i in range(1,abs(crab-average)+1):
            subtotal += i
        total += crab_quantities[crab] * subtotal

    return total


if __name__ == '__main__':
    Main()