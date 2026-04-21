class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 54ms
        # numbers = set()
        # for num in nums:
            
        #     if num in numbers:
        #         return True
        #     else:
        #         numbers.add(num)
        
        # return False

        # 38ms
        return len(set(nums)) != len(nums)