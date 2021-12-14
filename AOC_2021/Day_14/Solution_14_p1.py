import re
import copy


def main():
    starting_polymer, polymer_dict = Input_to_List('Day_14/Input_14.txt')
    polymer = starting_polymer
    
    for _ in range(10):
        pair_list = Get_Pairs(polymer)
        polymer = Insert_Element(pair_list, polymer_dict)

    char_counts = Count_Characters(polymer)
    maximum, minimum = Max_And_Min(char_counts)
    print(maximum - minimum)
    


def Input_to_List(path):

    # match_string = r"\w"

    file = open(path, 'r')
    starting_polymer = file.readline().strip()
    # coordinate = re.findall(match_string, line)

    line = file.readline().strip()
    line = file.readline().strip()

    polymer_dict = {}

    while True:
        if not line:
            break
        else:
            polymer_dict[line[0:2]] = line[-1]
            line = file.readline().strip()
            

    return starting_polymer, polymer_dict


def Get_Pairs(polymer):
    polymer_as_list = list(polymer)
    pair_list = []

    for index,character in enumerate(polymer_as_list):
        if index == 0:
            continue
        else:
            pair_list.append(polymer_as_list[index-1] + character)

    return pair_list


def Insert_Element(pair_list, polymer_dict):
    
    new_pair_list = [pair_list[0][0]]
    for pair in pair_list:
        insert = polymer_dict[pair]
        new_pair_list.append(insert + pair[1])
    
    return ''.join(new_pair_list)


def Count_Characters(polymer):
    letter_counts = {}

    for character in polymer:
        try:
            letter_counts[character] += 1
        except:
            letter_counts[character] = 1
    
    return letter_counts


def Max_And_Min(char_counts):
    maximum = 0
    minimum = 999999

    for letter in char_counts:
        if char_counts[letter] > maximum:
            maximum = char_counts[letter]
        if char_counts[letter] < minimum:
            minimum = char_counts[letter]
    
    return maximum, minimum


if __name__ == '__main__':
    main()