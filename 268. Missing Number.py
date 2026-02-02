class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        sum_n = sum(range(n))
        return sum_n - sum(nums)
        