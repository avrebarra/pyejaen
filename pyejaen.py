# import json


def parse(syntax):
    should_stop = False

    result = []
    syntax_tree = parse_tree(syntax)
    current_node = syntax_tree

    while should_stop == False:
        # print(current_node["value"])
        if "children" not in current_node:

            if "parent_ref" not in current_node:
                should_stop = True
                break

            result.append(current_node["value"])

            # move back to parent, delete visited children
            current_node = current_node["parent_ref"]
            current_node["children"].pop(0)
            if len(current_node["children"]) == 0:
                current_node.pop("children", None)

        else:
            # add ref to parent to enable backward movements for  unvisited node
            if "visited" not in current_node:
                for child in current_node["children"]:
                    child["parent_ref"] = current_node
                current_node["visited"] = True

            # dive to first children
            current_node = current_node["children"][0]

    # print result
    return result


def parse_tree(syntax):
    # tree helper functions
    def make_node(parent, value):
        return {
            "parent": parent,
            "value": value,
        }

    def add_child(node, child):
        if "children" not in node:
            node["children"] = []

        node["children"].append(child)

    # actual function
    root = make_node(True, "")  # root/parent object
    current_node = root

    # flags
    should_merge_letters = False

    # step = 1
    # depth = 0

    for char in syntax:
        # print('\ninput found: {}'.format(char))
        # Upon finding "(" or OPEN_STACK
        if char == "(":
            node = make_node(current_node, "")
            add_child(current_node, node)

            current_node = node
            # depth += 1

        # Upon finding ")" or CLOSE_STACK
        elif char == ")":
            current_node["parent"]["value"] += current_node["value"]

            parent = current_node["parent"]
            current_node.pop("parent", None)

            if should_merge_letters or len(current_node["children"]) <= 1:
                current_node.pop("children", None)
                should_merge_letters = False
                pass

            current_node = parent

            # depth -= 1

        # Upon finding "!" or MERGE_LETTERS
        elif char == "!":
            should_merge_letters = True

        # Upon finding LETTERS
        else:
            node = make_node(current_node, char)
            add_child(current_node, node)
            node.pop("parent", None)

            current_node["value"] += char

        # print("step {} depth {}".format(step, depth))
        # if len(current_node["value"]) > 0 and char != ")":
        #     print("value \"{}\"".format(current_node["value"]))
        # step += 1

    # print("")
    # print(json.dumps(root, indent=2))

    return root
