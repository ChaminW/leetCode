# This is the solution of No.1 problem in LeetCode, https://leetcode.com/problems/two-sum
# This is the brute force approach. In worst case scenario it's time complexity is O(n^2).
# There are optimized approaches.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1,index2]
        return []

nums = map(int,raw_input()[1:-1].split(","))
target = input()

print Solution().twoSum(nums,target)