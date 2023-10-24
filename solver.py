import solver_funcs


def get_cages():
    cagenum = int(input('Number of cages: '))
    cagelist = []
    i = 0
    lol = 0

    while i < cagenum:
        cage = input('Cage number %d: ' % lol).split()
        yasscage = [int(c) for c in cage]
        cagelist.append(yasscage)
        i += 1
        lol += 1

    return cagelist


def main():
    cages = get_cages()
    print('\n--Solution--\n')

    checks = 0
    colnum = 0
    rownum = 0
    counter = 0
    backtracks = 0
    puzzle = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    while counter < 25:
        rownum = counter // 5
        colnum = counter % 5
        puzzle[rownum][colnum] += 1

        if puzzle[rownum][colnum] > 5:
            backtracks += 1
            puzzle[rownum][colnum] = 0
            counter -= 1
        else:
            checks += 1
            if solver_funcs.check_valid(puzzle, cages):
                counter += 1

    for i in puzzle:
        print(*i)

    print('\nchecks: %d backtracks: %d' % (checks, backtracks))


if __name__ == '__main__':
    main()
