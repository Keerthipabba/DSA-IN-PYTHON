from collections import deque

def infix_to_postfix(expression):
    def get_precedence(op):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        return precedence.get(op, 0)

    output = []
    stack = deque()

    for token in expression:
        if token.isnumeric():  # if the token is an operand (number ie ABC OR 123)
            output.append(token)
        elif token == '(':  # left parenthesis
            stack.append(token)
        elif token == ')':  # right parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '(' from stack
        else:  # operator
            while stack and stack[-1] != '(' and get_precedence(stack[-1]) >= get_precedence(token):
                output.append(stack.pop())
            stack.append(token)

    # pop all the operators left in the stack
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Example usage
expression = "3+5*2/(7-2)"
print(f"Infix: {expression}")
print(f"Postfix: {infix_to_postfix(expression)}")