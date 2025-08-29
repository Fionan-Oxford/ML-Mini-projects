"""Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:

Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []"""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: None = None):
        self.val = val
        self.next = next


def arr2ll(arr: List[int]) -> Optional[ListNode]:

    dummy: ListNode | None = ListNode()
    tail: ListNode | None = dummy
    for a in arr:
        tail.next = ListNode(a)
        tail = tail.next

    return dummy.next


def ll2arr(head: Optional[ListNode]) -> List[int]:
    out: List[int] = []

    while head:
        out.append(head.val)
        head = head.next

    return out


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array: List[int] = ll2arr(head)
        array.reverse()

        return arr2ll(array)


head = [1, 2, 3, 4, 5]
mySolution = Solution()

print(ll2arr(mySolution.reverseList(arr2ll(head))))
