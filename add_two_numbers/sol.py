# Definition of singly-linked list
# class ListNode:
#   def _init_(self, x):
#       self.val = x
#       self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        ans = ptr = ListNode(0)
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            carry += num1 + num2
            ptr.next = ListNode(carry % 10)
            carry = carry // 10
            ptr = ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            ptr.next = ListNode(carry)

        return ans.next
