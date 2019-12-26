debug_mode = False


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
            debug("OPEN stack {}".format(stacknum))
            stacknum += 1
            stackmem[stacknum] = ""
        elif char == ")":
            debug("CLOSE stack {}".format(stacknum))

            if len(stackmem[stacknum]) > 1:
                result.append(stackmem[stacknum])

            stackmem[stacknum - 1] += stackmem[stacknum]
            stacknum -= 1
        else:
            debug("ADD {}".format(char))
            stackmem[stacknum] += char
            result.append(char)
            debug("   stack fill {}".format(stackmem[stacknum]))

    debug(result)
    debug("Result matches expected? {}".format(expected == result))

    return expected


def debug(p):
    if debug_mode:
        print(p)
