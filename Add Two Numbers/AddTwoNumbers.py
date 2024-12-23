# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def listToLinkedlist(self,l):
        head = ListNode(l[0])
        current = head
        for i in range(1,len(l)):
            current.next = ListNode(l[i])
            current = current.next
            

        # while head:
        #     print(head.val, end=" -> ")
        #     head = head.next
        # print("\n")

        return head


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        print("hi")
        head = ListNode(0)
        current= head
        carry = 0

        while l1 or l2 or carry:
            print("hi")

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            result = val1 + val2 + carry

            carry = result // 10
            current.next = ListNode(result % 10)

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        result = head.next
        while result:
            print(result.val, end=" -> ")
            result = result.next

        return head.next
        

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

L = ListNode()
ll1 = L.listToLinkedlist(l1)
ll2 = L.listToLinkedlist(l2)




S = Solution()

S.addTwoNumbers(l1=ll1, l2=ll2)