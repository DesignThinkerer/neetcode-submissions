# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         # 54ms
#         # numbers = set()
#         # for num in nums:
            
#         #     if num in numbers:
#         #         return True
#         #     else:
#         #         numbers.add(num)
        
#         # return False

#         # 38ms
#         return len(set(nums)) != len(nums)


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=[]
        for num in nums:
            if num in d:
                return True
            else:
                d.append(num)
        return False
