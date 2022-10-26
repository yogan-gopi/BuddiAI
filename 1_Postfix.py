#1_Postfix.py

def evaluate(postfix):
    postfix = postfix.split()
    stack = []
    op = "+-*/%"
    for i in postfix:
        if i not in op:
            stack.append(int(i))
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(eval("{}{}{}".format(n1, i, n2)))
    return stack[0]


if __name__ == '__main__':
    postfix = "100 200 + 2 / 5 * 7 +"
    print("The result for the Postfix expression: '{}' is {}".format(postfix, evaluate(postfix)))