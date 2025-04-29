class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # for i in nums:
        #     if i in count:
        #         count[i] +=1
        #     else:
        #         count[i] =1
        # return max(count, key = count.get)
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        majority = None
        max_ = float('-inf')
        for i in count:
            if count[i] > max_:
                max_ = count[i]
                majority = i
        return majority

            
            