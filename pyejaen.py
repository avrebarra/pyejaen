def parse(syntax):
    # "((a)((ya)(m)))"
    expected = ["a", "y", "a", "ya", "m", "yam", "ayam"]

    stackmem = {}
    stacknum = 0
    result = []

    # fill base stack
    stackmem[stacknum] = ""

    for char in syntax:
        if char == "(":
            print("OPEN stack {}".format(stacknum))
            stacknum += 1
            stackmem[stacknum] = ""
        elif char == ")":
            print("CLOSE stack {}".format(stacknum))
            result.append(stackmem[stacknum])
            stackmem[stacknum - 1] += stackmem[stacknum]
            stacknum -= 1
        else:
            print("ADD {}".format(char))
            stackmem[stacknum] += char
            print("   stack fill {}".format(stackmem[stacknum]))

    print(result)
    print("Result matches expected? {}".format(expected == result))

    return expected
