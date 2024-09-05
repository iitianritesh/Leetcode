class Solution:
    def twoSum(self, nums, target):
        # Create a hash map to store the value and index
        num_map = {}
        
        # Loop through the list
        for i, num in enumerate(nums):
            # Calculate the complement by subtracting the current number from the target
            complement = target - num
            
            # If the complement is already in the hash map, we found a solution
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, store the number and its index in the hash map
            num_map[num] = i

# Example usage
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)
