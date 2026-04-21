class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # freq_buckets[i] will store numbers that appear 'i' times
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq_buckets[c].append(n)
        
        res = []
        # Iterate backwards through buckets to get highest frequencies first
        for i in range(len(freq_buckets) - 1, 0, -1):
            for n in freq_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res