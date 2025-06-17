class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff = -1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j:
                    diff = nums[j] - nums[i]
                    if diff > max_diff:
                        max_diff = diff

        
        return max_diff if max_diff > 0 else -1
    

S = Solution()

print(S.maximumDifference([7, 1, 5, 4])) 