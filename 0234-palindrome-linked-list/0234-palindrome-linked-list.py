# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half_start = slow
        if fast: 
             second_half_start = slow.next
        newHead = self.reverseList(second_half_start) 
        first = head
        second = newHead
        is_palindrome = True
        
        while second:
            if first.val != second.val:
                is_palindrome = False
                break
            first = first.next
            second = second.next
        self.reverseList(newHead)

        return is_palindrome