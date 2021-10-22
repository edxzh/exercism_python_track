def is_paired(input_string):
    opened = "[{("
    closed = "]})"
    stack = []

    for char in input_string:
        if char in opened:
            stack.append(char)
        elif char in closed:
            if len(stack) == 0 or opened[closed.index(char)] != stack.pop():
                return False

    return len(stack) == 0
