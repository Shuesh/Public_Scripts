from tkinter import Tk
from tkinter.filedialog import askopenfilename

#Get the file path via a file explorer window
def Gui_File_Path():
    Tk().withdraw()
    filename = askopenfilename()
    if not filename:
        raise Exception("No file selected")
    return filename

#Basically a map function. Entries start as string/char type. Can change to int, float, etc. using a lambda function
def Input_to_List(path, num_headings, function = lambda a : a):

    if (num_headings < 0) or type(num_headings) is not int:
        raise TypeError("Number of headings only allows positive integer values")

    file = open(path,'r')
    
    headings = []
    for _ in range(num_headings):
        headings.append(file.readline().strip())

    input_list = []

    line = file.readline()
    while line:
        if line.strip():
            try:
                input_list.append(function(line.strip()))
            except:
                raise Exception("Lambda function error")
        line = file.readline()

    file.close()
    if num_headings > 0:
        return headings, input_list
    else:
        return input_list

#lines contain multiple elements that form a list. Delimiter must be string or char type
def Input_to_List_of_Lists(path, num_headings, delimiter=' '):

    if (num_headings < 0) or type(num_headings) is not int:
        raise TypeError("Number of headings only allows positive integer values")

    file = open(path,'r')
    
    headings = []
    for _ in range(num_headings):
        headings.append(file.readline().strip())

    input_list = []

    line = file.readline()
    while line:
        if line.strip():
            line = line.strip().split(delimiter)
            input_list.append(line)
        line = file.readline()
        
    file.close()
    if num_headings > 0:
        return headings, input_list
    else:
        return input_list

#returns a dictionary with the number of appearances for each term in a list. Only works on 1D lists
def List_to_Freq_Dict(data):
    return_dict = {}

    for term in data:
        try:
            return_dict[term] += 1
        except:
            return_dict[term] = 1

    return return_dict

#this will keep a list of all the terms connected to a given term (in a tree or other type of nested structure)
#the expected format is as follows: [outer term, inner term]
def List_to_Tree_Dict(data):
    tree_dict = {}

    for term in data:
        try:
            tree_dict[term[0]].append(term[1])
        except:
            tree_dict[term[0]] = [term[1]]
    
    return tree_dict


if __name__ == '__main__':
    path = Gui_File_Path() 
    print(path)
    print(Input_to_List(path, 1))
    # print(Input_to_List(path, 0, lambda a : int(a)))
    print(Input_to_List_of_Lists(path, 1,' -> '))