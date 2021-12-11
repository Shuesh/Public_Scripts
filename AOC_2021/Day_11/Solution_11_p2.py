import re

def main():
    octopus_list = Input_to_List('Day_11/Input_11.txt')
    count = 0
    step = 0
    while True:
        octopus_list = Step(octopus_list)
        octopus_list, count = Resolve(octopus_list, count)
        step += 1
        if (Check_Zeroes(octopus_list)):
            print(step)
            break

    print(count)



def Input_to_List(path):
    file = open(path, 'r')
    line = list(file.readline().strip())
    octopus_line = []
    for octopus in line:
        octopus_line.append(int(octopus))

    return_list = []

    while True:
        if not line:
            break
        else:
            return_list.append(octopus_line)
            line = list(file.readline().strip())
            octopus_line = []
            for octopus in line:
                octopus_line.append(int(octopus))

    return return_list



def Step(octopus_list):
    for row_index,row in enumerate(octopus_list):
        for octopus_index,octopus in enumerate(row):
            octopus_list[row_index][octopus_index] += 1
            if octopus > 8 and octopus < 99:
                octopus_list[row_index][octopus_index] = 100
                if row_index == 6:
                    temp = None
                octopus_list = Boom(octopus_list, row_index, octopus_index)

    return octopus_list



def Boom(octopus_list, row_index, octopus_index):
    for i in range(-1,2):
        for j in range(-1,2):
            try:
                if (row_index+i >= 0) and (octopus_index+j >= 0):
                    octopus_list[row_index+i][octopus_index+j] += 1
            except:
                continue

    for k in range(-1,2):
        for l in range(-1,2):
            try:
                if (octopus_list[row_index+k][octopus_index+l] > 9) and (octopus_list[row_index+k][octopus_index+l] < 100)\
                    and (row_index+k >= 0) and (octopus_index+l >= 0):

                    octopus_list[row_index+k][octopus_index+l] = 100
                    octopus_list = Boom(octopus_list, row_index+k, octopus_index+l)
            except:
                continue

    return octopus_list

    

def Resolve(octopus_list, count):

    for row_index,row in enumerate(octopus_list):
        for octopus_index,octopus in enumerate(row):
            if octopus > 99:
                count += 1
                octopus_list[row_index][octopus_index] = 0

    return octopus_list, count



def Check_Zeroes(octopus_list):
    all_zeroes = True
    for row in octopus_list:
        for octopus in row:
            if octopus != 0:
                all_zeroes = False
                break
        if all_zeroes == False:
            break
    return all_zeroes




if __name__ == '__main__':
    main()