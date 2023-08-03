# https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, node, k):
        vals = []
        vals_k = []

        while node:
            vals_k.insert(0, node.val)
            node = node.next
            if len(vals_k) == k:
                vals.extend(vals_k)
                vals_k = []
        vals.extend(vals_k[::-1])

        nodelist = None
        for i in range(len(vals)-1, -1, -1):
            nodelist = ListNode(vals[i], nodelist)

        return nodelist
