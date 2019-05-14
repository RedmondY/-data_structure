class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k or len(nums) == 0:
            return []

        n = len(nums)
        maxid = -1
        res = [0] * (n - k + 1)
        for i in range(n - k + 1):
            if maxid < i:  # 说明最大值不在当前滑动窗口内，本次需要重新在滑动窗口内计算最大值
                maxid = i
                for j in range(i, i + k):
                    if nums[j] >= nums[maxid]:
                        maxid = j
            else:
                if nums[maxid] <= nums[i + k - 1]:  # 当前最大值和滑动窗口最后一个元素比较
                    maxid = i + k - 1
            res[i] = nums[maxid]
        return res
