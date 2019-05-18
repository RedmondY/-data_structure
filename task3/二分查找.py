class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.searchDivide(nums, target, 0, len(nums) - 1)

    def searchDivide(self, nums, target, left, right):
        if target < nums[left] or target > nums[right] or left > right:
            return -1
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif nums[mid] > target:
            return self.searchDivide(nums, target, left, mid - 1)
        else:
            return self.searchDivide(nums, target, mid + 1, right)
