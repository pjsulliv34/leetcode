class Solution:
    def canJump(self, nums: List[int]) -> bool:    
        #check the length at each index, if the index > length, return false, we cant reach that index
        length = 0
        i = 0
        while i < len(nums):
            print(i)
            if i > length:
                return False
            else:
                length = max(i+nums[i], length)
            i +=1
        if length >= len(nums)-1:
            return True
                






    # Greedy O(N)
    #    goal = len(nums)-1
    #    for i in range(len(nums)-1,-1,-1):
    #     if i +nums[i]>= goal:
    #         goal = i
    #    if goal ==0:
    #     return True
    #    else:
    #     return False
    # Dynamic (o(n^2))
        # n = len(nums)
        # memo = {n-1:True}
        # def can_jump(i):
        #     if i in memo:
        #         return memo[i]
        #     for jump in range(1, nums[i]+1):
        #         if can_jump(i+jump):
        #             memo[i]=True
        #             return True
        #     memo[i] = False
        #     return False

        # return can_jump(0)

    #greedy
        # goal = len(nums)-1
        # for i in range(len(nums)-1, -1,-1):
        #     # print(i)
        #     if nums[i]+ i >= goal:
        #         goal = i
        # if goal ==0:
        #     return True
        # else: 
        #     return False
        # farthest = 0
        # if len(nums)==1:
        #     return True
        # for i in range(len(nums)-1):
        #     if i > farthest:
        #         return False
        #     farthest = max(farthest, i +nums[i])
        #     if farthest >= len(nums)-1:
        #         return True
        # return False
