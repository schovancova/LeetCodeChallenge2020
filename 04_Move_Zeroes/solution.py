class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lenn = len(nums)
        i = 0
        while i < lenn:
            if nums[i]:
                i += 1
                continue
            nums.pop(i)
            nums.extend([0])
            lenn -= 1
