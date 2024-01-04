class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Initialize an empty dictionary
        dic = {}
        # Count the appearance of the elements
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        # Initialize the answer
        ans = 0
        # For the number of appearance of numbers
        for value in dic.values():
            if value<2: # There is no way to eliminate a single number, return -1
                return -1
            else:
                while value>3:
                    ans+=1
                    value = value-3 # Eliminate three appearance
                # Outside the while-loop, three conditions might appear:
                # 1. [3,3,3] We eliminate three of them with one operation
                # 2. [3,3] We eliminate two of them with one operation
                # 3. [3] We eliminate one less element in the last operation, leaving[3,3],
                # and that belongs to number 2

                # In all three conditions, we need one extra operation, so answer +=1
                ans+=1 
        return ans
            
