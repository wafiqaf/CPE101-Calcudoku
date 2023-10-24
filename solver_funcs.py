def check_valid(puzzle, cages):
    if check_columns_valid(puzzle):
        if check_rows_valid(puzzle):
            if check_cages_valid(puzzle, cages):
                return True
    return False


def check_cages_valid(puzzle, cages):
    for i in cages:
        if check_one_cage(i, puzzle) is False:
            return False
    return True


def check_one_cage(cage, puzzle):
    newcage = []
    sum1 = 0

    for i in range(2, len(cage)):
        row = cage[i] // 5
        col = cage[i] % 5
        sum1 += puzzle[row][col]
        newcage.append(puzzle[row][col])
    if ((sum1 < cage[0] and newcage.count(0) >= 1)
            or (sum1 == cage[0] and newcage.count(0) == 0)):
        return True

    return False

#    sumofcage = 0
#    full = True
#    sum1 = 0
#
#    for num in range(2, len(cage)):
#        sum1 = puzzle[cage[num] // 5][cage[num] % 5]
#        sumofcage += sum1
#        if sum1 == 0:
#            full = False
#
#    if sumofcage == cage[0] or sumofcage < cage[0] and not full:
#        return True
#
#    return False


def check_columns_valid(puzzle):
    colmnew = []
    lisnum = 0
    colnum = 0
    counter = 0

    while counter < 5:
        for i in range(len(puzzle)):
            colmnew.append(puzzle[lisnum][colnum])
            lisnum += 1
        if check_one_col(colmnew) is False:
            return False
        colnum += 1
        counter += 1
        lisnum = 0
        colmnew = []

    return True


def check_one_col(col):
    coldupes = []
    for i in col:
        if i in coldupes:
            if i == 0:
                pass
            else:
                return False
        coldupes.append(i)
    return True


def check_rows_valid(puzzle):
    for i in puzzle:
        if check_one_row(i) is False:
            return False
    return True


def check_one_row(row):
    rowdupes = []
    for i in row:
        if i in rowdupes:
            if i == 0:
                pass
            else:
                return False
        rowdupes.append(i)
    return True
