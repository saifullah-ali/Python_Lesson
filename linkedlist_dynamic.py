# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val, nextNode=None):
        #node object having two attributes - val and nextNode
        self.val = val
        self.nextNode = nextNode
class LinkList(object):
    def __init__(self, head = None):
        self.head = head
        print(f'head {self.head}')
    
    def insert(self, val):
        node = ListNode(val) #creating node object
        #print(node.val)
        if self.head is None: #this only applicable once we first create LinkList object and insert first value of node
            self.head = node  # refering self.head to its own (the first object/node) 
            print(f'head {self.head}') # So self.head is always the first node node1. head wont change once set
            return

        currentNode = self.head # this is applicable for any further insertion other than first insert
        # currentNode will always be the head node i.e. node1
        while True:
            if currentNode.nextNode is None: # as once we are at node2, still node1's nextNode haven't been set yet
                currentNode.nextNode = node  # setting up node1's nextNode to node2(node)
                print(f'checking {node}')
                break
            
            currentNode = currentNode.nextNode #this is set once currentNode.nextNode is not None, so it traverses throught the nodes

    def printLinkedList(self):
        currentNode = self.head
        print(f'Testing grep next next node val {currentNode.nextNode.nextNode.val}')
        while currentNode is not None:
            print(f'{currentNode.val} -->{currentNode} to {currentNode.nextNode}')
            currentNode = currentNode.nextNode
        print("None")



d = LinkList()
d.insert(1)
d.insert(2)
#d.printLinkedList()
d.insert(3)
d.insert(10)
d.insert(10)
d.insert(3)
d.insert(2)
d.insert(1)
d.printLinkedList()

#print(d.head)

class Solution(object):
    def isPalindrome(self, head):
        fast = slow = head
        # find the mid node
        while fast and fast.nextNode: #this is how we get the middle node as 'slow'
            fast = fast.nextNode.nextNode
            slow = slow.nextNode
            print(f'fast is {fast} and slow is {slow}')
         # reverse the second half
        node = None
        while slow:
            nxt = slow.nextNode
            slow.nextNode = node #reversing
            node = slow
            slow = nxt
            print(f'line 67:: nxt {nxt} node {node} slow {slow}')
        # compare the first and second half nodes
        while node: # while node and head:
            print(f' node val {node.val} head val {head.val}')
            if node.val != head.val:
                return False
            node = node.nextNode
            head = head.nextNode
        return True

s = Solution()

print(s.isPalindrome(d.head))