import re
import copy
import time


def main():
    starting_polymer, polymer_dict = Input_to_List('Day_14/Input_14.txt')
    polymer = starting_polymer

    pair_counts = Get_Pairs(polymer)
    
    for _ in range(40):
        # print(_+1)
        # start = time.time()
        pair_counts = Get_Pair_Counts(pair_counts, polymer_dict)
        # end = time.time()
        # print(end-start, 'seconds')

    char_counts = Count_Characters(pair_counts, starting_polymer)
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
    pair_dict = {}

    for index,character in enumerate(polymer_as_list):
        if index == 0:
            continue
        else:
            pair_list.append(polymer_as_list[index-1] + character)


    for pair in pair_list:
        try:
            pair_dict[pair] += 1
        except:
            pair_dict[pair] = 1

    return pair_dict


def Get_Pair_Counts(pair_counts, polymer_dict):
    new_pair_counts = {}

    for key in pair_counts:
        try:
            new_pair_counts[key[0] + polymer_dict[key]] += pair_counts[key]
        except:
            new_pair_counts[key[0] + polymer_dict[key]] = pair_counts[key]

        try: 
            new_pair_counts[polymer_dict[key] + key[1]] += pair_counts[key]
        except:
            new_pair_counts[polymer_dict[key] + key[1]] = pair_counts[key]

    return new_pair_counts


def Count_Characters(pair_counts, starting_polymer):
    letter_counts = {}

    for key in pair_counts:
        try:
            letter_counts[key[0]] += pair_counts[key]
        except:
            letter_counts[key[0]] = pair_counts[key]
    
        try:
            letter_counts[key[1]] += pair_counts[key]
        except:
            letter_counts[key[1]] = pair_counts[key]

    for letter in letter_counts:
        letter_counts[letter] = letter_counts[letter] // 2    

    letter_counts[starting_polymer[0]] += 1
    letter_counts[starting_polymer[-1]] += 1

    return letter_counts


def Max_And_Min(char_counts):
    maximum = 0
    minimum = 999999999999999

    for letter in char_counts:
        if char_counts[letter] > maximum:
            maximum = char_counts[letter]
        if char_counts[letter] < minimum:
            minimum = char_counts[letter]
    
    return maximum, minimum


if __name__ == '__main__':
    main()