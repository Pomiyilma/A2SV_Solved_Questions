class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        # list to linkedlist 
        dummy = ListNode()    #turns lists into Linked lists!!!
        curr = dummy               # -> 13 -> 8, the # is dummy (basically null)   
        for value in stack:         
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next    #return the head
