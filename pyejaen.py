debug_mode = False


def parse(syntax):
    stack = {}
    result = []

    stackdepth = 0

    # fill base stack
    stack[stackdepth] = ""

    for char in syntax:
        if char == "(":
            stackdepth += 1
            stack[stackdepth] = ""
        elif char == ")":
            if len(stack[stackdepth]) > 1:
                result.append(stack[stackdepth])

            stack[stackdepth - 1] += stack[stackdepth]
            stackdepth -= 1
        else:
            stack[stackdepth] += char
            result.append(char)

    return result


def debug(p):
    if debug_mode:
        print(p)
