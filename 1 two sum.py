class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {v:i for i,v in enumerate(nums)}
        # print(num_dict)
        for i,v in enumerate(nums):
            diff = target - v
            # print(diff)
            # print(i)
            if diff in num_dict and i != num_dict[diff]:
                return [i,num_dict[diff]]
