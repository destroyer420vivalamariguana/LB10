#
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def eval(self):

        if self.right is not None and self.left is not None :
            if self.value == '+':
                return self.left.eval() + self.right.eval()
            elif self.value == '*':
                return self.left.eval() * self.right.eval()

        else:
            return float(self.value)

#################################
# First Case :  (5+3)*6
#
#         *
#     +      6
#   5   3
#################################
def evalManual():
    opeNodeA = Node(5)
    opeNodeB = Node(3)

    sumNode = Node('+')
    sumNode.left = opeNodeA
    sumNode.right = opeNodeB

    opeNodeC = Node(6)
    mulNode = Node('*')
    mulNode.left = sumNode
    mulNode.right = opeNodeC

    print(mulNode.eval())

#################################
# Main
#################################
if __name__ == '__main__':
    '''
    Este metodo es para 
    '''
    evalManual()
   # evalPostfixExpression()
   # convertIndorToPostfixExp()
   # evalIndorExpression()


