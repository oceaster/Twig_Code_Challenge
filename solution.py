

def divide_sequence(seq, sets):
    size = int(len(seq) / sets)
    curr = 0
    out = [list(), ]

    for value in seq:
        if curr >= size and len(out) < sets:
            curr = 0
            out.append(list())
        out[-1].append(value)
        curr += 1

    return out


if __name__ == "__main__":
    '''
    tests that the declared function 'divide_sequence' works as
    intended when file is run as main and given value from terminal argument.
    Eg. python solution.py 5
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
