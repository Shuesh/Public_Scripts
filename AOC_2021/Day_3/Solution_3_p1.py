def main():
    binary_list = Input_to_List('Day_3/Input_3.txt')
    (gamma,epsilon) = Gamma_Epsilon_Finder(binary_list)
    dec_gamma = Convert_to_Decimal(gamma)
    dec_epsilon = Convert_to_Decimal(epsilon)
    print(dec_gamma * dec_epsilon)


def Input_to_List(path):
    file = open(path, 'r')
    line = file.readline()

    return_list = []

    while (line != ''):
        return_list.append(line.strip())
        line = file.readline()

    return return_list

def Gamma_Epsilon_Finder(binary_list):
    zeroes_count = [0 for _ in binary_list[0]]
    ones_count = [0 for _ in binary_list[0]]

    for term in binary_list:
        for index,digit in enumerate(term):
            if digit == '1':
                ones_count[index] += 1
            else:
                zeroes_count[index] += 1

    gamma = ''
    epsilon = ''
    for i,term in enumerate(zeroes_count):
        if zeroes_count[i] > ones_count[i]:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        else:
            gamma = gamma + '1'
            epsilon = epsilon + '0'

    return (gamma,epsilon)


# for binary STRINGS
def Convert_to_Decimal(binary):
    total =  0
    length = len(binary)

    for index,digit in enumerate(binary):
        total += int(digit) * 2 ** (length - index - 1)

    return total


if __name__ == '__main__':
    main()