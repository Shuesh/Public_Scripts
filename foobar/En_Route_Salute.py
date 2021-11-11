def solution(s):
    s = s.replace("-","")
    return salute_count(s)


def salute_count(s):
    count = 0
    length = len(s)

    for index,soldier in enumerate(s):
        if (soldier == '>'):
            for position in range(index+1, length):
                if s[position] == '<':
                    count += 2

    return count


solution('>-----<')