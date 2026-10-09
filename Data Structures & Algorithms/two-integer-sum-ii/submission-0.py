class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for index, num in enumerate(numbers):
            hashMap[num] = index
        
        for index, num in enumerate(numbers):
            if target-num in hashMap:
                return [index+1, hashMap[target-num]+1]
            
        