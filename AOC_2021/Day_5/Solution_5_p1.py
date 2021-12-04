def main():
    input_list = Input_to_List('Day_5/Example_5.txt')
    output_list = Function(input_list)
    print(output_list)


def Input_to_List(path):
    file = open(path, 'r')
    line = file.readline()

    return_list = []

    while (line != ''):
        return_list.append(line.strip())
        line = file.readline()

    return return_list

def Function(input_list):
    pass


# for binary STRINGS
def Convert_to_Decimal(binary):
    total =  0
    length = len(binary)

    for index,digit in enumerate(binary):
        total += int(digit) * 2 ** (length - index - 1)

    return total


if __name__ == '__main__':
    main()