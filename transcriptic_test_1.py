__author__ = "Joshua Hancock"


# Dictionaries used.
row_dict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
invert_row_dict = {v: k for k, v in row_dict.items()}
row_range = ["A", "B", "C", "D", "E", "F", "G", "H"]


# robotize takes a numerical input and returns the address of a well on a 96 well plate.
def robotize(well):
    if well in range(0, 96):
        row = well / 12
        column = (well % 12) + 1
        return row_dict[row] + str(column)
    else:
        return "Outside range, please enter an integer between 0 and 95"


# humanize takes an address input of a well on a 96 well plate and returns a numerical value.
def humanize(well):
    if well[0] in row_range and int(well[1:]) in range(1, 13):
        row = well[0]
        address = well[1:]
        row = invert_row_dict[row] * 12
        address = row + (int(address) - 1)
        return address


# this function asserts that robotize reference and humanize reference equal the same address.
def test_conversions():
    for i in range(0, 96):
        assert(i == humanize((robotize(i))))
        print "Well %s converts to %s" % (humanize(robotize(i)), robotize(i))


test_conversions()
