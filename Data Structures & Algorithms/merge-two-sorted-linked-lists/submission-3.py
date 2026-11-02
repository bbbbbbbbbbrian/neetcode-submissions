# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2

        if ptr1 == None and ptr2 == None:
            return ptr1

        if ptr1 == None:
            combined_list = ptr2
            start = combined_list
            ptr2 = ptr2.next
            while ptr2 != None:
                combined_list.next = ptr2
                ptr2 = ptr2.next
                combined_list = combined_list.next
            return start
        elif ptr2 == None:
            combined_list = ptr1
            start = combined_list
            ptr1 = ptr1.next
            while ptr1 != None:
                combined_list.next = ptr1
                ptr1 = ptr1.next
                combined_list = combined_list.next
            return start
        elif ptr1.val >= ptr2.val:
            combined_list = ptr2
            ptr2 = ptr2.next
        else:
            combined_list = ptr1
            ptr1 = ptr1.next

        start = combined_list

        while(ptr1 != None and ptr2 != None):
            if ptr1.val >= ptr2.val:
                combined_list.next = ptr2
                ptr2 = ptr2.next
            else:
                combined_list.next = ptr1
                ptr1 = ptr1.next
            combined_list = combined_list.next

        if ptr1 == None:
            while ptr2 != None:
                combined_list.next = ptr2
                ptr2 = ptr2.next
                combined_list = combined_list.next
        elif ptr2 == None:
            while ptr1 != None:
                combined_list.next = ptr1
                ptr1 = ptr1.next
                combined_list = combined_list.next
        return start

