# https://leetcode.com/problems/add-two-numbers/

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = temp = ListNode(999)
        carry = 0
        while l1 or l2 or carry:
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            tempSum = temp1 + temp2 + carry
            if tempSum >= 10:
                carry = 1
                temp.next = ListNode(tempSum % 10)
                temp = temp.next
            else:
                temp.next = ListNode(tempSum)
                temp = temp.next
                carry = 0
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next