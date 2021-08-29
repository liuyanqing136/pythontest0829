class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        var = str(self.val) + ' '
        next = self.next
        while (next != None):
            var += str(next.val) + ' '
            next = next.next
        return var

    def fuzhi(self, l):
        result = None
        nextnode = None
        for i in range(len(l) - 1, -1, -1):
            l13 = ListNode(l[i], None)
            if nextnode != None:
                l13.next = nextnode
            nextnode = l13
            result = l13
        return l13


class Solution(ListNode):
    def mergeTwoList(self, l1: ListNode, l2: ListNode):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoList(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoList(l1, l2.next)
            return l2


if __name__ == '__main__':
    obj = Solution()
    l1 = [1, 2, 3]
    l2 = [2, 3, 4]
    l11 = obj.fuzhi(l1)
    l21 = obj.fuzhi(l2)

    result = obj.mergeTwoList(l11, l21)
    print(result)
