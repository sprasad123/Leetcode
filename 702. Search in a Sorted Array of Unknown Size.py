# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        n = 1
        while reader.get(n) != 2**31 - 1:
            n *= 2
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                l = mid + 1
            else:
                r = mid - 1
        if reader.get(l) == target:
            return l
        if reader.get(r) == target:
            return r
        return -1
        