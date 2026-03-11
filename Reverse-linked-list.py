class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:  #while head isn't null
            next_node = curr.next  #next_node = 2
            curr.next = prev   #curr.next is none (1(curr)'s next is none after it's reversed)
            prev = curr  #prev = 1, curr = none
            curr = next_node   #curr = 2

        return prev
