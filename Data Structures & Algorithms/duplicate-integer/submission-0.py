class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums = set()
        for i in nums:
            setnums.add(i)
        if len(setnums) < len(nums):
            return True
        return False
        