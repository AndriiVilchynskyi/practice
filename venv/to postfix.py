OPERATORS = {'+', '-', '*', '/', '(', ')', '^'}  # set of operators

PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities


def toPostFixExpression(expression):  # input expression

    stack = []  # initially stack empty

    output = []  # initially output empty

    for ch in expression:

        if ch not in OPERATORS:  # if an operand then put it directly in postfix expression

            output += ch

        elif ch == '(':  # else operators should be put in stack

            stack.append('(')

        elif ch == ')':

            while stack and stack[-1] != '(':
                output += stack.pop()

            stack.pop()

        else:

            # lesser priority can't be on top on higher or equal priority

            # so pop and put in output

            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()

            stack.append(ch)

    while stack:
        output += stack.pop()

    return output

a = toPostFixExpression(["2","+","3"])
b = toPostFixExpression(["20","+","3","*","(","5","*","4",")"])
print(a)
print(b)