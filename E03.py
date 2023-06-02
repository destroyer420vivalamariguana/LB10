operatorPrecedence = {
    '(': 0,
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}


def postfixConvert(infix):
    stack = []
    postfix = []

    for char in infix:
        if char not in operatorPrecedence:
            postfix.append(char)
        else:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack[-1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()
                elif operatorPrecedence[char] > operatorPrecedence[stack[-1]]:
                    stack.append(char)
                else:
                    while len(stack) != 0:
                        if stack[-1] == '(':
                            break
                        postfix.append(stack.pop())
                    stack.append(char)

    while len(stack) != 0:
        postfix.append(stack.pop())

    return "".join(postfix)

#################################
# Third Case :  Convert indor to
#               postfix expression
# Indor expression   : (5+3)*6
# Postfix expression : 53+6*
#################################
def convertIndorToPostfixExp():
    indor = "(5+3)*6"
    postfix = postfixConvert(indor) # “53+6*”
    print(postfix)
#################################
# Main
#################################
if __name__ == '__main__':
    '''
    Este metodo es para 
    '''
    # evalManual()
    # evalPostfixExpression()
    convertIndorToPostfixExp()
    # evalIndorExpression()
    # evalIndorExpressionFromKeyboard()
