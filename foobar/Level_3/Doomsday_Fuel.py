# Test cases:
#   [0, 2, 1, 0, 0] 
#   [0, 0, 0, 3, 4] 
#   [0, 0, 0, 0, 0] 
#   [0, 0, 0, 0, 0]
#   [0, 0, 0, 0, 0]
# Output: [7, 6, 8, 21], where S2 = 7/21, S3 = 6/21, and S8 = 8/21

    # [0, 1, 0, 0, 0, 1]
    # [4, 0, 0, 3, 2, 0]
    # [0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0]
# Output = [0, 3, 2, 9, 14]

#The ore starts in state 0
#The matrix is always square

import copy

def solution(m):
    terminal_states = [True for _ in m]
    reverse_lookup = [[] for _ in m]

    for i,row in enumerate(m):
        for term in row:
            if term != 0:
                terminal_states[i] = False
                break
        if terminal_states[i] == False:
            m[i] = probability(row)
        
        if type(m[i][0]) is list:
            for index,fraction in enumerate(row):
                if fraction[0] != 0:
                    reverse_lookup[index].append(fraction)
    
    
    print(m)
    print(reverse_lookup)


    


def probability(row):
    total = 0
    for item in row:
        total += item

    returnable_row = [None for _ in row]
    for i,item in enumerate(row):
        returnable_row[i] = [item, total]

    return returnable_row


#def generate_probabilities(matrix):



solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])