class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for num in nums:
            required = target - num
            if required in nums:
                if required == num:
                    loc1 = nums.index(num)
                    numsCopy = nums.copy()
                    print("numsCopy, nums:",numsCopy, nums)
                    numsCopy.pop(loc1)
                    print("numsCopy, nums:",numsCopy, nums)
                    if required in numsCopy:
                        return [loc1, numsCopy.index(required)+1]
                else:
                    print("required:",required)
                    print("nums:",nums)
                    return [nums.index(num), nums.index(required)]
        return [0,0]