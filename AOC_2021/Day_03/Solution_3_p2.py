def main():
    binary_list = Input_to_List('Day_3/Input_3.txt')
    (o2,co2) = O2_CO2_Finder(binary_list, binary_list, 0)
    dec_o2 = Convert_to_Decimal(o2)
    dec_co2 = Convert_to_Decimal(co2)
    print(dec_o2 * dec_co2)


def Input_to_List(path):
    file = open(path, 'r')
    line = file.readline()

    return_list = []

    while (line != ''):
        return_list.append(line.strip())
        line = file.readline()

    return return_list

def O2_CO2_Finder(o2_list, co2_list, index):
    o2_zeroes_count = 0
    o2_ones_count = 0
    o2_new_list = []
    co2_zeroes_count = 0
    co2_ones_count = 0
    co2_new_list = []

    if (len(o2_list) > 1):
        for term in o2_list:
            if term[index] == '1':
                o2_ones_count += 1
            else:
                o2_zeroes_count += 1

    if (len(co2_list) > 1):
        for term in co2_list:
            if term[index] == '1':
                co2_ones_count += 1
            else:
                co2_zeroes_count += 1


    if o2_ones_count > o2_zeroes_count:
        greater = '1'
    elif o2_zeroes_count > o2_ones_count:
        greater = '0'
    else:
        greater = 'equal'

    if co2_ones_count > co2_zeroes_count:
        lesser = '0'
    elif co2_zeroes_count > co2_ones_count:
        lesser = '1'
    else:
        lesser = 'equal'

    if (len(o2_list) > 1):
        for term in o2_list:
            if term[index] == greater:
                o2_new_list.append(term)
            elif greater == 'equal' and term[index] == '1':
                o2_new_list.append(term)
    
    if (len(co2_list) > 1):
        for term in co2_list:
            if term[index] == lesser:
                co2_new_list.append(term)
            elif lesser == 'equal' and term[index] == '0':
                co2_new_list.append(term)

    if (len(o2_list) == 1):
        o2_new_list = o2_list
    if (len(co2_list) == 1):
        co2_new_list = co2_list

    if (len(o2_new_list) > 1 or len(co2_new_list) > 1):
        return O2_CO2_Finder(o2_new_list, co2_new_list, index+1)
    else:
        return(o2_new_list[0], co2_new_list[0])


# for binary STRINGS
def Convert_to_Decimal(binary):
    total =  0
    length = len(binary)

    for index,digit in enumerate(binary):
        total += int(digit) * 2 ** (length - index - 1)

    return total


if __name__ == '__main__':
    main()