class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            compl = target - num
            if compl in hashmap:
                return [hashmap[compl], i]
            hashmap[num] = i