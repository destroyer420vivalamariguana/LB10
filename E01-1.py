class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def eval(self):

        if self.right is not None and self.left is not None:
            if self.value == '+':
                return self.left.eval() + self.right.eval()
            elif self.value == '*':
                return self.left.eval() * self.right.eval()
            elif self.value == '-':
                return self.left.eval() - self.right.eval()
            elif self.value == '/':
                return self.left.eval() / self.right.eval()

        else:
            return float(self.value)


#################################
# First Case :  (5-3)-(6*4)/(4+2)
#
#           -
#     -          /
#   5   3    *         +
#         6    4    4     2
#################################
def evalManual():
    opeNodeA = Node(5)
    opeNodeB = Node(3)
    restNode = Node('-')
    restNode.left = opeNodeA
    restNode.right = opeNodeB

    opeNodeC = Node(6)
    opeNodeD = Node(4)
    mulNode = Node('*')
    mulNode.left = opeNodeC
    mulNode.right = opeNodeD

    opeNodeE = Node(6)
    opeNodeF = Node(4)
    sumNode = Node('+')
    sumNode.left = opeNodeC
    sumNode.right = opeNodeD

    opeNodeE = Node(4)
    opeNodeF = Node(2)
    sumNode = Node('+')
    sumNode.left = opeNodeE
    sumNode.right = opeNodeF

    divNode = Node('/')
    divNode.left = mulNode
    divNode.right = sumNode

    resNode = Node('-')
    resNode.right = divNode
    resNode.left = restNode

    print(resNode.eval())


if __name__ == '__main__':
    '''
    Este metodo es para 
    '''
    evalManual()
    # evalPostfixExpression()
    # convertIndorToPostfixExp()
    # evalIndorExpression()