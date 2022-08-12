import math
import string

import pandas


def column_to_number(c) -> int:
    """Return number corresponding to excel-style column name."""
    num = 0
    for letter in c:
        assert letter in string.ascii_letters

        num *= 26
        num += ord(letter.upper()) - 64
    return num


def column_to_string(n) -> str:
    """Return excel-style column name corresponding to number."""
    name = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        name = chr(65 + remainder) + name
    return name.upper()


def get_data(column_letters: str, ignore_empty=True):
    print("> Reading data for [{}]".format(column_letters))

    column_letters = column_letters.replace(" ", "")

    requested_order = list()
    for section in column_letters.split(','):
        if ':' in section:
            letter_range = section.split(':')
            range_start = column_to_number(letter_range[0])
            range_end = column_to_number(letter_range[1])
            if range_start <= range_end:
                requested_order.extend(list(range(range_start, range_end + 1)))
            else:
                requested_order.extend(reversed(list(range(range_end, range_start + 1))))
        else:
            requested_order.append(column_to_number(section))

    expected_order = sorted(requested_order)

    xls = pandas.read_excel(
        './input/дані стаття освіта+податки.xlsx',
        skiprows=2,
        usecols="A,B,{}".format(",".join(map(lambda num: column_to_string(num), expected_order)))
    )

    ids = list()
    names = list()
    points = list()

    for i, row in xls.iterrows():
        r_id = None
        r_name = None
        r_point = list([0] * (row.size - 2))

        for j, cell in enumerate(row):
            if j == 0:
                r_id = cell
            elif j == 1:
                r_name = cell
            else:
                if math.isnan(cell):
                    if ignore_empty:
                        r_point = None
                        break
                    else:
                        continue

                r_point[requested_order.index(expected_order[j - 2])] = cell

        if r_point:
            ids.append(r_id)
            names.append(r_name)
            points.append(r_point)

    assert ids.__len__() == names.__len__() and names.__len__() == points.__len__()

    return {
        "Columns": list(map(lambda c: column_to_string(c), requested_order)),
        "C_Ids": ids,
        "C_Names": names,
        "C_Points": points
    }
