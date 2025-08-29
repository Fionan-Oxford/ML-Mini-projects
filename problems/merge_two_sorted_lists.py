"""You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: None = None):
        self.val = val
        self.next = next


def array2LL(arr: List[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy

    for a in arr:
        tail.next = ListNode(a)
        tail = tail.next

    return dummy.next


def ll2array(ll: ListNode | None) -> List | None:

    head = ll
    out: List[int] = []

    while head:
        out.append(head.val)
        head = head.next

    return out


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        array1: List[int] | None = ll2array(list1)
        array2: List[int] | None = ll2array(list2)

        print(array1, array2)

        out: List[int] = []

        if array1:
            for a in array1:
                out.append(a)

        if array2:
            for b in array2:
                out.append(b)

        out.sort()
        return array2LL(out)


list1 = [1, 2, 4]
list2 = [1, 3, 4]

mySolution = Solution()
print(ll2array(mySolution.mergeTwoLists(array2LL(list1), array2LL(list2))))
