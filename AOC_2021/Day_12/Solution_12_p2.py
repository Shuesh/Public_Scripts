import re


valid_paths = []

def main():
    input_dict = Input_to_List('Day_12/Input_12.txt')
    valid_paths = Recursive_Search(input_dict, ['start'], False)
    print(len(valid_paths))

    

def Input_to_List(path):
    #Gets all caves
    match_string = r"[a-zA-Z]+"

    file = open(path, 'r')
    line = file.readline()
    caves = re.findall(match_string, line)

    return_dict = {}

    while True:
        if not line:
            break
        else:
            try:
                return_dict[caves[0]].append(caves[1])
            except:
                return_dict[caves[0]] = [caves[1]]
            
            try:
                return_dict[caves[1]].append(caves[0])
            except:
                return_dict[caves[1]] = [caves[0]]

            line = file.readline()
            caves = re.findall(match_string, line)        

    for cave in return_dict:
        return_dict[cave].sort()

    return return_dict



#Depth first
def Recursive_Search(input_dict, path, double_small):
    if path[-1] == 'end':
        return path
    else:
        for cave in input_dict[path[-1]]:
            double_small = Check_Double_Small(path)
            if cave[0].isupper() or (cave[0].islower() and cave not in path and cave != 'start') or (not double_small and cave != 'start'):
                temp = path + [cave]
                finished_path = Recursive_Search(input_dict, temp, double_small)
                if finished_path != None and finished_path != [] and finished_path[-1] == 'end':
                    valid_paths.append(finished_path)
    
    return valid_paths


def Check_Double_Small(path):
    for index,cave in enumerate(path):
        if cave[0].islower():
            for other in path[index+1:]:
                if cave == other:
                    return True
    return False
    

if __name__ == '__main__':
    main()