class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def eval(self):
        if self.right is not None and self.left is not None:
            if self.value == '*':
                return self.left.eval() * self.right.eval()
            elif self.value == '/':
                return self.left.eval() / self.right.eval()
            elif self.value == '-':
                return self.left.eval() - self.right.eval()
            elif self.value == '^':
                return self.left.eval() ** self.right.eval()
        else:
            return float(self.value)

operatorPrecedence = {
    '(': 0,
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 2
}

def parserPostfixToBinaryTree(postfix):
    stack = []
    for char in postfix:
        if char not in operatorPrecedence:
            node = Node(char)
            stack.append(node)
        else:
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack.pop()

def evalPostfixExpression():
    postfix = "53-64*42-/-2^"
    rootNode = parserPostfixToBinaryTree(postfix)
    print(rootNode.eval())

#################################
# Main
#################################
if __name__ == '__main__':
    '''
    Este metodo es para
    '''
    # evalManual()
    evalPostfixExpression()