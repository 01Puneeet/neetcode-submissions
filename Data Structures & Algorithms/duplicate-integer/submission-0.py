class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = []
        a = len(nums)
        for i in range(a):
            b = nums[i]
            if b not in ans:
                ans.append(b)
            else:
                return True
        return False
        