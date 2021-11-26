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

import numpy as np

def solution(m):
    terminal_state_bools = [True for _ in m]
    reverse_lookup = [[] for _ in m]

    for i,row in enumerate(m):
        for term in row:
            if term != 0:
                terminal_state_bools[i] = False
                break
        if terminal_state_bools[i] == False:
            m[i] = generate_fractions(row, i)
        
        if type(m[i][0]) is list:
            for index,fraction in enumerate(m[i]):
                if fraction[0] != 0:
                    reverse_lookup[index].append(fraction)

    terminal_states = []
    probabilities = []
    for j,state in enumerate(terminal_state_bools):
        if state == True:
            terminal_states.append(j)
    
    probabilities = generate_probabilities(reverse_lookup, terminal_states)
    
    print(m)
    print(reverse_lookup)
    print(probabilities)


def generate_fractions(row, state):
    total = 0
    for item in row:
        total += item

    returnable_row = [None for _ in row]
    for i,item in enumerate(row):
        returnable_row[i] = [item, total, state]

    return returnable_row


def generate_probabilities(lookup_matrix, terminal_states):
    final_probabilities = [[] for _ in terminal_states]

    for i,state in enumerate(terminal_states):
        for fraction in lookup_matrix[state]:
            if fraction[2] == 0:
                final_probabilities[i].append(fraction[:2])
            else:
                final_probabilities[i].append(recurse(lookup_matrix,fraction))


def recurse(lookup_matrix, fraction):
    pass

def add(fraction1, fraction2):
    temp1 = [fraction1[0] * fraction2[1], fraction1[1] * fraction2[1]]
    temp2 = [fraction1[1] * fraction2[0], fraction1[1] * fraction2[1]]

    return [temp1[0] + temp2[0], temp1[1]]

def multiply(fraction1, fraction2):
    return [fraction1[0]*fraction2[0], fraction1[1] * fraction2[1]]

def rebase(args_list):
    new_denominator = 0

    denominators = []
    for fraction in args_list:
        if fraction[0] != 0:
            denominators.append(fraction[1])

    lcm = np.lcm(denominators)
    for fraction in args_list:
        pass




solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])