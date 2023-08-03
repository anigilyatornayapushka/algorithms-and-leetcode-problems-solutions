# https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution №1

class Solution:
    def mergeKLists(self, lists):
        res = []
        
        for l in lists:
            while l:
                res.append(l.val)
                l = l.next

        def fill(nums):
            if not nums:
                return None
            nodelist = ListNode(nums[0])
            nodelist.next = fill(nums[1:])
            return nodelist

        ret = fill(sorted(res))
        
        return ret

# Solution №2

class Solution:
    def mergeKLists(self, lists):
        res = []
        
        for l in lists:
            while l:
                res.append(l.val)
                l = l.next

        vals = sorted(res, reverse=True)
        nodelist = None
        for n in vals:
            nodelist = ListNode(n, nodelist)

        return nodelist
