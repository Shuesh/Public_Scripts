def solution(M, F):
    generations = calculate(int(M), int(F))
    print(generations)

#Does it make more sense to work backwards? Yes. This is the way it should be done, 
#however recursive functions will make the call stack too large if we use simple subtraction
def recursive_search(M, F):
    print(M, F)
    if (M == 1 and F == 1):
        return 0
    elif (M==1):
        return F-1
    elif (F==1):
        return M-1
    elif (M > F):
        return 1 + recursive_search(M-F, F)
    elif (M < F):
        return 1 + recursive_search(M, F-M)

def calculate(M, F):
    generations = 0

    while not (M == 1 and F == 1):
        if (M <= 0 or F <= 0):
            return 'impossible'
        if (M == 1):
            generations += F - 1
            break
        elif (F == 1):
            generations += M - 1
            break
        elif (M > F):
            generations += M // F
            M = M % F
        elif (F > M):
            generations += F // M
            F = F % M

    return generations

solution(52579,123456789123456789)