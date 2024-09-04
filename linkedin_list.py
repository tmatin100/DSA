class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    def printNode(self):
        print("node value", self.data)
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end=' -> ')
            currentNode = currentNode.next
        print()
    def insertAtBeginning(self, value):
        newNode = Node(value)
        if self.head is None:
            # list is empty, the new node itself is head and tail
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def insertAtEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            last_node = self.tail
            last_node.next = newNode
            self.tail = newNode
    def insertAtMiddle(self, insertAfter, value):
        if self.head is None:
            print("linkedlist is empty, cannot find ", insertAfter)
            return
        currentNode = self.head
        while currentNode and currentNode.data != insertAfter:
            currentNode = currentNode.next
        # fails when currentNode = None
        # fails when currentNode.data == insertAfter
        newNode = Node(value)
        if currentNode is not None:
            tmp = currentNode.next
            currentNode.next = newNode
            newNode.next = tmp
        else:
            print("cannot find ", insertAfter)


node1 = Node(100)
print(node1.next)
node2 = Node(200)
node3 = Node(300)



# 100 -> 200 -> 300
# link the nodes
node1.next = node2
node1.next.printNode()
node2.next = node3
node2.next.printNode()

# create a linkedList
head, tail = node1, node3
linkedList = SinglyLinkedList()
linkedList.printList()

# operations on LinkedList
linkedList.insertAtBeginning(400)
linkedList.printList()
linkedList.insertAtEnd(500)
linkedList.printList()
linkedList.insertAtMiddle(200, 600)
linkedList.printList()
linkedList.insertAtMiddle(1000, 700)
linkedList.insertAtMiddle(2000, 700)