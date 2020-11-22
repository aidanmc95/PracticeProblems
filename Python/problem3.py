from 'BaseStructures/LinkedList.py' import Node, LinkedList

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = None
        curr = head
        count = 0
        while(curr):
            curr = curr.next
            count += 1
        if count == n:
            return head.next
        print(count, n)
        curr = head
        for i in range(count - n):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head

