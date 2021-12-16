def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # Store symbols as encountered
    bracketStack = []

    # Traverse string and add each encountered symbol to stack
    for c in s:
        # Left symbols
        if c in ['(', '{', '[']:
            bracketStack.append(c)
        # Right symbols
        elif c == ')' and len(bracketStack) != 0 and bracketStack[-1] == '(':
            bracketStack.pop()
        elif c == ']' and len(bracketStack) != 0 and bracketStack[-1] == '[':
            bracketStack.pop()
        elif c == '}' and len(bracketStack) != 0 and bracketStack[-1] == '{':
            bracketStack.pop()
        # No valid symbols
        else:
            return False
    # Check is stack is empty
    return bracketStack == []

s = "([})"
print(isValid(s))