class Solution:
        def majorityElement(self, nums: List[int]) -> int:
            hash_map = {}
            n = len(nums)
            for num in nums:
                hash_map[num] = hash_map.setdefault(num, 0) + 1
                if hash_map[num] > n / 2:
                    return num
