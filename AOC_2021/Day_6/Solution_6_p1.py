import re

def main():
    fish_list = Input_to_List('Day_6/Input_6.txt')
    for _ in range(80):
        fish_list = decrement(fish_list)
    print(len(fish_list))


def Input_to_List(path):
    match_string = r"\d+"

    file = open(path, 'r')

    line = file.readline().strip()
    fish = re.findall(match_string, line)

    for i,angler in enumerate(fish):
        fish[i] = int(angler)

    return fish

def decrement(fish_list):
    
    for index,fish in enumerate(fish_list):
        if (fish > 0):
            fish_list[index] = fish - 1
        elif (fish == 0):
            fish_list[index] = 6
            fish_list.append(9)

    return fish_list

if __name__ == '__main__':
    main()