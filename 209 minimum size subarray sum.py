class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_array = 0
        min_length = float('inf')

        for i in range(len(nums)):
            print(i)
            sum_array += nums[i]
            print(f'current sub array {sum_array}')
            #if the subarray is >= target, we can shrink subarray vi
            while sum_array >=target:
                min_length = min(min_length, i- left +1)
                #After checking if min is smaller, now we reduce left to right
                sum_array -= nums[left]
                left +=1

        if min_length == float('inf'):
            return 0
        else:
            return min_length

        

       

        

