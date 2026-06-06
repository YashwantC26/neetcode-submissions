class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        answer = sorted(count, key=lambda x: count[x], reverse=True)
        return answer[:k]