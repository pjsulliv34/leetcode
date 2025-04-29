class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #method, use binary search, if keep searching to the left or right untile we find a peak
        #compare against the other elments

        l,r = 0 , len(nums)-1

        while l<r:
            mid = (r+l)//2
            print(mid)
            if nums[mid] > nums[mid+1]:
                #move to left
                r = mid
            else:
                l = mid +1
        return l