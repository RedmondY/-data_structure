class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        while low <= high:
            mid = (low + high) >> 1
            if mid * mid == x:
                return mid

            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
                if low * low > x:
                    return mid


class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            r = (r + x / r) >> 1
        return int(r)
