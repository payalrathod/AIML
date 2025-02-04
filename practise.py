from typing import List


class Solution:
    def twoSums(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i]+nums[j]:
                    return [i,j]

num = [3,3]
target = 6
s = Solution()
print(s.twoSums(num, target))