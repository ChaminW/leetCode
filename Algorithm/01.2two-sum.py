# This is the solution of No.1 problem in LeetCode, https://leetcode.com/problems/two-sum
# This approach uses hash maps(dictionary in python). This algo has O(n) time complexity.
# This is a optimized approach.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        buffer_dic = {}
        for index, key in enumerate(nums):
            if buffer_dic.has_key(key):
                return [buffer_dic[key] + 1, index + 1]
            else:
                buffer_dic[target - key] = index
        return []


nums = map(int, raw_input()[1:-1].split(","))
target = input()

print Solution().twoSum(nums, target)
