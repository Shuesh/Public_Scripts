import re

def main():
    fish_list = Input_to_List('Day_6/Input_6.txt')
    fish_groups = count_fish_categories(fish_list)
    for _ in range(256):
        fish_groups = decrement_groups(fish_groups)
    total = total_count(fish_groups)
    print(total)


def Input_to_List(path):
    match_string = r"\d+"

    file = open(path, 'r')

    line = file.readline().strip()
    fish = re.findall(match_string, line)

    for i,angler in enumerate(fish):
        fish[i] = int(angler)

    return fish

def count_fish_categories(fish_list):
    number_fish = [0 for _ in range(9)]

    for fish in fish_list:
        number_fish[fish] += 1

    return number_fish


def decrement_groups(fish_counts):
    groups_copy = [0 for _ in range(9)]

    #iterates backwards
    for index,count in enumerate(reversed(fish_counts)):
        groups_copy[7-index] = count
        if(index == 8):
            groups_copy[6] += count

    return groups_copy


def total_count(fish_groups):
    count = 0

    for term in fish_groups:
        count += term

    return count



if __name__ == '__main__':
    main()