VALID_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def solve2(numArray):
    return "hello"

def solve3(numArray):
    return "hello"

def solve4(numArray):
    index = 0
    solution = ""
    possibilities = []
    # addition possibilities, order does not matter
    possibilities.append([numArray[0] + numArray[1], numArray[2], numArray[3]], numArray[0], "+", numArray[1])
    possibilities.append([numArray[0] + numArray[2], numArray[1], numArray[3]], numArray[0], "+", numArray[2])
    possibilities.append([numArray[0] + numArray[3], numArray[1], numArray[2]], numArray[0], "+", numArray[3])
    possibilities.append([numArray[1] + numArray[2], numArray[0], numArray[3]], numArray[1], "+", numArray[2])
    possibilities.append([numArray[1] + numArray[3], numArray[0], numArray[2]], numArray[1], "+", numArray[3])
    possibilities.append([numArray[2] + numArray[3], numArray[0], numArray[1]], numArray[2], "+", numArray[3])

    # multiplication possibilities, order does not matter
    possibilities.append([numArray[0] * numArray[1], numArray[2], numArray[3]], numArray[0], "*", numArray[1])
    possibilities.append([numArray[0] * numArray[2], numArray[1], numArray[3]], numArray[0], "*", numArray[2])
    possibilities.append([numArray[0] * numArray[3], numArray[1], numArray[2]], numArray[0], "*", numArray[3])
    possibilities.append([numArray[1] * numArray[2], numArray[0], numArray[3]], numArray[1], "*", numArray[2])
    possibilities.append([numArray[1] * numArray[3], numArray[0], numArray[2]], numArray[1], "*", numArray[3])
    possibilities.append([numArray[2] * numArray[3], numArray[0], numArray[1]], numArray[2], "*", numArray[3])

    # subtraction possibilities, order matters!
    possibilities.append([numArray[0] - numArray[1], numArray[2], numArray[3]], numArray[0], "-", numArray[1])
    possibilities.append([numArray[0] - numArray[2], numArray[1], numArray[3]], numArray[0], "-", numArray[2])
    possibilities.append([numArray[0] - numArray[3], numArray[1], numArray[2]], numArray[0], "-", numArray[3])
    possibilities.append([numArray[1] - numArray[0], numArray[2], numArray[3]], numArray[1], "-", numArray[0])
    possibilities.append([numArray[1] - numArray[2], numArray[0], numArray[3]], numArray[1], "-", numArray[2])
    possibilities.append([numArray[1] - numArray[3], numArray[0], numArray[2]], numArray[1], "-", numArray[3])
    possibilities.append([numArray[2] - numArray[0], numArray[1], numArray[3]], numArray[2], "-", numArray[0])
    possibilities.append([numArray[2] - numArray[1], numArray[0], numArray[3]], numArray[2], "-", numArray[1])
    possibilities.append([numArray[2] - numArray[3], numArray[0], numArray[1]], numArray[2], "-", numArray[3])
    possibilities.append([numArray[3] - numArray[0], numArray[1], numArray[2]], numArray[3], "-", numArray[0])
    possibilities.append([numArray[3] - numArray[1], numArray[0], numArray[2]], numArray[3], "-", numArray[1])
    possibilities.append([numArray[3] - numArray[2], numArray[0], numArray[1]], numArray[3], "-", numArray[2])

    # division possibilities, order matters!
    possibilities.append([numArray[0] / numArray[1], numArray[2], numArray[3]], numArray[0], "/", numArray[1])
    possibilities.append([numArray[0] / numArray[2], numArray[1], numArray[3]], numArray[0], "/", numArray[2])
    possibilities.append([numArray[0] / numArray[3], numArray[1], numArray[2]], numArray[0], "/", numArray[3])
    possibilities.append([numArray[1] / numArray[0], numArray[2], numArray[3]], numArray[1], "/", numArray[0])
    possibilities.append([numArray[1] / numArray[2], numArray[0], numArray[3]], numArray[1], "/", numArray[2])
    possibilities.append([numArray[1] / numArray[3], numArray[0], numArray[2]], numArray[1], "/", numArray[3])
    possibilities.append([numArray[2] / numArray[0], numArray[1], numArray[3]], numArray[2], "/", numArray[0])
    possibilities.append([numArray[2] / numArray[1], numArray[0], numArray[3]], numArray[2], "/", numArray[1])
    possibilities.append([numArray[2] / numArray[3], numArray[0], numArray[1]], numArray[2], "/", numArray[3])
    possibilities.append([numArray[3] / numArray[0], numArray[1], numArray[2]], numArray[3], "/", numArray[0])
    possibilities.append([numArray[3] / numArray[1], numArray[0], numArray[2]], numArray[3], "/", numArray[1])
    possibilities.append([numArray[3] / numArray[2], numArray[0], numArray[1]], numArray[3], "/", numArray[2])

    for p in possibilities:
        solution = solve3(p)
        if solution != "false"
            return p

    return "No solution exists to the numbers inputted"


nums = input("Enter 4 numbers between 1 and 9 inclusive, with one space in between each one: ")
numArray = nums.strip().split(" ")

if len(numArray) != 4:
    print("Please provide exactly 4 numbers")
else:
    first = int(numArray[0])
    second = int(numArray[1])
    third = int(numArray[2])
    fourth = int(numArray[3])

    if first not in VALID_NUMBERS or second not in VALID_NUMBERS or \
        third not in VALID_NUMBERS or fourth not in VALID_NUMBERS:
        print("Please input only numbers between 1 and 9 inclusive")
    else:
        solution = solve4(numArray)
        print(solution)
