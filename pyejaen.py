debug_mode = False


def parse(syntax):
    stack = {}
    result = []

    stackdepth = 0

    # flags
    should_merge_letters = False

    # fill base stack
    stack[stackdepth] = ""

    for char in syntax:
        # Upon finding "(" or OPEN_STACK
        if char == "(":
            stackdepth += 1
            stack[stackdepth] = ""

        # Upon finding ")" or CLOSE_STACK
        elif char == ")":
            if len(stack[stackdepth]) > 1:
                result.append(stack[stackdepth])

            stack[stackdepth - 1] += stack[stackdepth]
            stackdepth -= 1

            # clear flags
            should_merge_letters = False

        # Upon finding "!" or MERGE_LETTERS
        elif char == "!":
            should_merge_letters = True

        # Upon finding LETTERS
        else:
            if not should_merge_letters:
                result.append(char)

            stack[stackdepth] += char

    return result


def debug(p):
    if debug_mode:
        print(p)
