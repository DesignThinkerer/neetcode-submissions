class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # on small list, turning the list to a set 
        # and comparing length is faster, 
        # but on big dataset building a set (On) 
        # and checking for existence (O1) is faster
        # because we can break early
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            else:
                num_set.add(n)
        return False