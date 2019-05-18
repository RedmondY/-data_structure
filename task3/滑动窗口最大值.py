class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        tmp = max(nums[:k])
        result = [tmp]
        for i in range(k, len(nums)):
            if nums[i] > tmp:
                tmp = nums[i]
            elif nums[i - k] == tmp:
                tmp = max(nums[i - k + 1:i + 1])
            result.append(tmp)
        return result
