

def divide_sequence(seq, sets):
    '''
    :seq: takes list or set as declaration for original sequence    
    :sets:  takes integer as declaration for amount of new 
            equally sized arrays
    :return: array of lists containing parts of original array 
            with total length declared by sets parameter 
    '''
    size = len(seq) / sets
    curr = 0
    out = [list(), ]
    
    if size > int(size):                # Adjust var for unequally sized divisons
        size = int(size) + 1

    for value in seq:
        if curr == size:
            curr = 0
            out.append(list())
        if curr < size:
            out[-1].append(value)
        curr += 1

    return out


if __name__ == "__main__":
    ''' 
    tests that the declared function 'divide_array' works as
    intended when file is run as main and given value from terminal argument.
    
    Eg. python twig_code_challenge.py 5
    
    '''
    from sys import argv

    if len(argv) > 1:
        sets = int(argv[1])
    else:
        sets = 5

    print(
        divide_sequence(
            seq=(1,2,3,4,5,6,7,8,9,10),
            sets=sets
        )
    )
