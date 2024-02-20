# Power of 2: 19/02/2024
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 or n%2 != 0:
            return False
        else:
            return self.isPowerOfTwo(n//2)
    
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            if nums[i]==i:
                continue
            else:
                return i
            
    

# print(Solution().isPowerOfTwo(3))
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))

    