# valid numbers to begin with
VALID_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def solve2(numArray):
    """
    Given an array of two numbers (and additional elements for how we got there), 
    see if it is possible to get to 24.
    If it is, return how it was done. If not, return "false".
    Zeroes and negative numbers are not allowed.
    """
    if numArray[0] < 1 or numArray[1] < 1:
        return "false"

    if (numArray[0] + numArray[1] == 24):
        print(str(numArray[0]) + " + " + str(numArray[1]) + " = 24")
        return str(numArray[0]) + " + " + str(numArray[1]) + " = 24"
    if (numArray[0] * numArray[1] == 24):
        print(str(numArray[0]) + " * " + str(numArray[1]) + " = 24")
        return str(numArray[0]) + " * " + str(numArray[1]) + " = 24"
    if (numArray[0] - numArray[1] == 24):
        print(str(numArray[0]) + " - " + str(numArray[1]) + " = 24")
        return str(numArray[0]) + " - " + str(numArray[1]) + " = 24"
    if (numArray[0] / numArray[1] == 24):
        print(str(numArray[0]) + " / " + str(numArray[1]) + " = 24")
        return str(numArray[0]) + " / " + str(numArray[1]) + " = 24"
    if (numArray[1] - numArray[0] == 24):
        print(str(numArray[1]) + " - " + str(numArray[0]) + " = 24")
        return str(numArray[1]) + " - " + str(numArray[0]) + " = 24"
    if (numArray[1] / numArray[0] == 24):
        print(str(numArray[1]) + " / " + str(numArray[0]) + " = 24")
        return str(numArray[1]) + " / " + str(numArray[0]) + " = 24"

    return "false"

def solve3(numArray):
    """
    Given an array of 3 numbers (and additional elements for how we got there), 
    call solve2() on all possible combinations of numbers and operations to 
    see if it is possible to get to 24. Iterate through all possibilities, returning
    the solution if it is possible, and "false" if it is not.
    Zeroes and negative numbers not allowed in computation of the solution
    """
    if numArray[0] < 1 or numArray[1] < 1 or numArray[2] < 1:
        return "false"

    possibilities = []
    # addition possibilities, order does not matter
    possibilities.append([numArray[0] + numArray[1], numArray[2], numArray[0], "+", numArray[1]])
    possibilities.append([numArray[0] + numArray[2], numArray[1], numArray[0], "+", numArray[2]])
    possibilities.append([numArray[1] + numArray[2], numArray[0], numArray[1], "+", numArray[2]])

    # multiplication possibilities, order does not matter
    possibilities.append([numArray[0] * numArray[1], numArray[2], numArray[0], "*", numArray[1]])
    possibilities.append([numArray[0] * numArray[2], numArray[1], numArray[0], "*", numArray[2]])
    possibilities.append([numArray[1] * numArray[2], numArray[0], numArray[1], "*", numArray[2]])

    # subtraction possibilities, order matters!
    possibilities.append([numArray[0] - numArray[1], numArray[2], numArray[0], "-", numArray[1]])
    possibilities.append([numArray[0] - numArray[2], numArray[1], numArray[0], "-", numArray[2]])
    possibilities.append([numArray[1] - numArray[0], numArray[2], numArray[1], "-", numArray[0]])
    possibilities.append([numArray[1] - numArray[2], numArray[0], numArray[1], "-", numArray[2]])
    possibilities.append([numArray[2] - numArray[0], numArray[1], numArray[2], "-", numArray[0]])
    possibilities.append([numArray[2] - numArray[1], numArray[0], numArray[2], "-", numArray[1]])

    # division possibilities, order matters!
    possibilities.append([numArray[0] / numArray[1], numArray[2], numArray[0], "/", numArray[1]])
    possibilities.append([numArray[0] / numArray[2], numArray[1], numArray[0], "/", numArray[2]])
    possibilities.append([numArray[1] / numArray[0], numArray[2], numArray[1], "/", numArray[0]])
    possibilities.append([numArray[1] / numArray[2], numArray[0], numArray[1], "/", numArray[2]])
    possibilities.append([numArray[2] / numArray[0], numArray[1], numArray[2], "/", numArray[0]])
    possibilities.append([numArray[2] / numArray[1], numArray[0], numArray[2], "/", numArray[1]])

    for p in possibilities:
        solution = solve2(p)
        if solution != "false":
            if p[3] == "+":
                print(p)
                return str(p[2]) + " + " + str(p[4]) + " = " + str(p[2] + p[4]) + ", " + solution
            elif p[3] == "*":
                print(p)
                return str(p[2]) + " * " + str(p[4]) + " = " + str(p[2] * p[4]) + ", " + solution
            elif p[3] == "-":
                print(p)
                return str(p[2]) + " - " + str(p[4]) + " = " + str(p[2] - p[4]) + ", " + solution
            else:
                print(p)
                return str(p[2]) + " / " + str(p[4]) + " = " + str(p[2] / p[4]) + ", " + solution

    return "false"

def solve4(numArray):
    """
    Given an array of 4 numbers, create an array of all possible combinations of numbers and operations.
    Then, call solve3() on each possibility, which will in turn call solve2() on all of those possibilities
    to determine if it is possible to get to 24 from the given input. If it is possible, it will return the
    steps taken to get to the solution. Otherwise, it will return that it is not possible to get to 24
    from the given input.
    """
    possibilities = []
    # addition possibilities, order does not matter
    possibilities.append([numArray[0] + numArray[1], numArray[2], numArray[3], numArray[0], "+", numArray[1]])
    possibilities.append([numArray[0] + numArray[2], numArray[1], numArray[3], numArray[0], "+", numArray[2]])
    possibilities.append([numArray[0] + numArray[3], numArray[1], numArray[2], numArray[0], "+", numArray[3]])
    possibilities.append([numArray[1] + numArray[2], numArray[0], numArray[3], numArray[1], "+", numArray[2]])
    possibilities.append([numArray[1] + numArray[3], numArray[0], numArray[2], numArray[1], "+", numArray[3]])
    possibilities.append([numArray[2] + numArray[3], numArray[0], numArray[1], numArray[2], "+", numArray[3]])

    # multiplication possibilities, order does not matter
    possibilities.append([numArray[0] * numArray[1], numArray[2], numArray[3], numArray[0], "*", numArray[1]])
    possibilities.append([numArray[0] * numArray[2], numArray[1], numArray[3], numArray[0], "*", numArray[2]])
    possibilities.append([numArray[0] * numArray[3], numArray[1], numArray[2], numArray[0], "*", numArray[3]])
    possibilities.append([numArray[1] * numArray[2], numArray[0], numArray[3], numArray[1], "*", numArray[2]])
    possibilities.append([numArray[1] * numArray[3], numArray[0], numArray[2], numArray[1], "*", numArray[3]])
    possibilities.append([numArray[2] * numArray[3], numArray[0], numArray[1], numArray[2], "*", numArray[3]])

    # subtraction possibilities, order matters!
    possibilities.append([numArray[0] - numArray[1], numArray[2], numArray[3], numArray[0], "-", numArray[1]])
    possibilities.append([numArray[0] - numArray[2], numArray[1], numArray[3], numArray[0], "-", numArray[2]])
    possibilities.append([numArray[0] - numArray[3], numArray[1], numArray[2], numArray[0], "-", numArray[3]])
    possibilities.append([numArray[1] - numArray[0], numArray[2], numArray[3], numArray[1], "-", numArray[0]])
    possibilities.append([numArray[1] - numArray[2], numArray[0], numArray[3], numArray[1], "-", numArray[2]])
    possibilities.append([numArray[1] - numArray[3], numArray[0], numArray[2], numArray[1], "-", numArray[3]])
    possibilities.append([numArray[2] - numArray[0], numArray[1], numArray[3], numArray[2], "-", numArray[0]])
    possibilities.append([numArray[2] - numArray[1], numArray[0], numArray[3], numArray[2], "-", numArray[1]])
    possibilities.append([numArray[2] - numArray[3], numArray[0], numArray[1], numArray[2], "-", numArray[3]])
    possibilities.append([numArray[3] - numArray[0], numArray[1], numArray[2], numArray[3], "-", numArray[0]])
    possibilities.append([numArray[3] - numArray[1], numArray[0], numArray[2], numArray[3], "-", numArray[1]])
    possibilities.append([numArray[3] - numArray[2], numArray[0], numArray[1], numArray[3], "-", numArray[2]])

    # division possibilities, order matters!
    possibilities.append([numArray[0] / numArray[1], numArray[2], numArray[3], numArray[0], "/", numArray[1]])
    possibilities.append([numArray[0] / numArray[2], numArray[1], numArray[3], numArray[0], "/", numArray[2]])
    possibilities.append([numArray[0] / numArray[3], numArray[1], numArray[2], numArray[0], "/", numArray[3]])
    possibilities.append([numArray[1] / numArray[0], numArray[2], numArray[3], numArray[1], "/", numArray[0]])
    possibilities.append([numArray[1] / numArray[2], numArray[0], numArray[3], numArray[1], "/", numArray[2]])
    possibilities.append([numArray[1] / numArray[3], numArray[0], numArray[2], numArray[1], "/", numArray[3]])
    possibilities.append([numArray[2] / numArray[0], numArray[1], numArray[3], numArray[2], "/", numArray[0]])
    possibilities.append([numArray[2] / numArray[1], numArray[0], numArray[3], numArray[2], "/", numArray[1]])
    possibilities.append([numArray[2] / numArray[3], numArray[0], numArray[1], numArray[2], "/", numArray[3]])
    possibilities.append([numArray[3] / numArray[0], numArray[1], numArray[2], numArray[3], "/", numArray[0]])
    possibilities.append([numArray[3] / numArray[1], numArray[0], numArray[2], numArray[3], "/", numArray[1]])
    possibilities.append([numArray[3] / numArray[2], numArray[0], numArray[1], numArray[3], "/", numArray[2]])

    for p in possibilities:
        solution = solve3(p)
        if solution != "false":
            if p[4] == "+":
                print(p)
                return str(p[3]) + " + " + str(p[5]) + " = " + str(p[3] + p[5]) + ", " + solution
            elif p[4] == "*":
                print(p)
                return str(p[3]) + " * " + str(p[5]) + " = " + str(p[3] * p[5]) + ", " + solution
            elif p[4] == "-":
                print(p)
                return str(p[3]) + " - " + str(p[5]) + " = " + str(p[3] - p[5]) + ", " + solution
            else:
                print(p)
                return str(p[3]) + " / " + str(p[5]) + " = " + str(p[3] / p[5]) + ", " + solution

    return "No solution exists to the numbers inputted"

# program while loop tries to get to 24 based on user inputted numbers, and exits on "exit" 
while True:
    nums = input('Enter 4 numbers between 1 and 9 inclusive, with one space in between each one. Enter "exit" to stop: ')
    if nums == "exit":
        break

    numArray = nums.strip().split(" ")

    # must be exactly 4 numbers
    if len(numArray) != 4:
        print("Please provide exactly 4 numbers")
    else:
        first = numArray[0] = int(numArray[0])
        second = numArray[1] = int(numArray[1])
        third = numArray[2] = int(numArray[2])
        fourth = numArray[3] = int(numArray[3])

        # each number must be 1-9 inclusive
        if first not in VALID_NUMBERS or second not in VALID_NUMBERS or \
            third not in VALID_NUMBERS or fourth not in VALID_NUMBERS:
            print("Please input only numbers between 1 and 9 inclusive")
        else:
            solution = solve4(numArray)
            print(solution)
