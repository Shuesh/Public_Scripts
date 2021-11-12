def solution(x,y):
    #makes a triangular structure
    # num_rows = x + y - 1
    # triangle = list_maker(num_rows)
    # print(str(triangle[y-1][x-1]))
    print(tree_sum(x,y) + x)


# def list_maker(maximum):
    # counter = 0
    # value = 1
    # triangle = [[] for x in range(maximum)]

    # counter tracks the column
    # while (counter < maximum):
        # want an x and y position to track individually. These should always sum to counter
        # counter_y = counter
        # counter_x = 0
        # while (counter_y >= 0):
            # triangle[counter_y].append(value)
            # value += 1
            # counter_y -= 1
            # counter_x += 1
        # counter += 1

    # return triangle


def tree_sum(x,y):
    halfway = (x+y-2) // 2
    #if even
    if ((x+y) % 2 == 0):
        sum = (halfway * (x+y-1))
    #if odd
    else:
        sum = (halfway * (x+y-1) + halfway + 1)
    return sum


solution(4,6)