class linkedListNode:#example of linked list - manual
    def __init__(self, value, nextNode=None):
        #Each object wikk have two attributes, value and nextNode
        self.value = value
        self.nextNode = nextNode

#creating object for each node
node1 = linkedListNode("3")
node2 = linkedListNode("4")
node3 = linkedListNode("5")
node4 = linkedListNode("8")

# this will define nextNode attribute of each object
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

currentNode = node1

while  True:#infinite loop
    print(currentNode.value)
    print(f'currentNode location {currentNode} and nextNode location {currentNode.nextNode}')
    if currentNode.nextNode is None:        
        print("None")
        break
    currentNode = currentNode.nextNode

print('this implies, nodes are like a box (see each iteration nextNode object location = next iteration current node object location is same')
print(f'Tesing next next attribure {node1.nextNode.nextNode} and its value {node1.nextNode.nextNode.value}')