class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        
        self.head = Node(0)
        self.tail = Node(0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        
        node = Node(value)
        
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node
        
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        
        node = Node(value)
        
        node.prev = self.tail.prev
        node.next = self.tail
        
        self.tail.prev.next = node
        self.tail.prev = node
        
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        
        node = self.head.next
        
        self.head.next = node.next
        node.next.prev = self.head
        
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        
        node = self.tail.prev
        
        self.tail.prev = node.prev
        node.prev.next = self.tail
        
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.head.next.val

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
