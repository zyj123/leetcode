# -*- coding: utf-8 -*- #
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = temp = ListNode(0)
        carry = False
        while l1 or l2 or carry:
            temp.next = ListNode(0)
            temp = temp.next
            if l1:
                temp.val += l1.val
                l1 = l1.next
            if l2:
                temp.val += l2.val
                l2 = l2.next
            if carry:
                temp.val += 1
                carry = False
            if temp.val > 9:
                temp.val -= 10
                carry = True
        res = res.next
        return res
def list_to_listnode(l):
    l1 = temp = ListNode(0)
    for i in l:
        temp.next = ListNode(0)
        temp = temp.next
        temp.val = i
    l1 = l1.next
    return l1

l1 = [5]
l2 = [5]
l1 = list_to_listnode(l1)
l2 = list_to_listnode(l2)

obj = Solution();
res = obj.addTwoNumbers(l1, l2)
while True:
    if res:
        print(res.val)
        res = res.next
    else:
        break