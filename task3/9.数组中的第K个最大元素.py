class Solution(object):
    def findKthLargest(self, nums, k):
        return self.search(nums, 0, len(nums) - 1, k)

    def search(self, nums, start, end, k):
        m = self.partition(nums, start, end)
        if m == k - 1:
            return nums[m]
        elif m > k - 1:
            return self.search(nums, start, m - 1, k)
        else:
            return self.search(nums, m + 1, end, k)

    def partition(self, nums, start, end):
        base = nums[start]
        pl = start
        pr = end
        while pl < pr:
            while pl < pr and nums[pr] <= base:
                pr -= 1

            if pl == pr:
                break
            else:
                nums[pl], nums[pr] = nums[pr], nums[pl]

            while pl < pr and nums[pl] >= base:
                pl += 1

            if pl == pr:
                break
            else:
                nums[pl], nums[pr] = nums[pr], nums[pl]

        nums[pl] = base
        return pl
