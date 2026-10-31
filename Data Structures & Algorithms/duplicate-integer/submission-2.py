class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        variety = {}
        for num in nums:
            if num in variety:
                return True
            else:
                variety[num] = 1
        return False