class Solution:
    def hasDuplicateHashSet(self, nums: list[int]) -> bool:
        '''
        We can use a set to keep track of the numbers we have seen so far while iterating through the list
        Time Complexity: O(n) if the whole list doesn't have duplicates
        Space Complexity: O(n) since if the whole list doesn' have duplicates, then seen will have a size of n
        '''
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
    
    def hasDuplicateBruteForce(self, nums: list[int]) -> bool:
        '''
        We can have a nested loop inside of a for loop to compare the i_th number with each number after it
        Time Complexity: O(n^2) because if the whole list doesn't have duplicates, then the nested loop will run n times for each iteration of the outer loop
        Space Complexity: O(1) since we aren't storing extra memory
        '''
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def hasDuplicateSorted(self, nums: list[int]) -> bool:
        '''
        We sort the list first, and then iterate through it. Checking the current number with the number in front of it
        Time Complexity: O(nlogn) because we have to sort the list
        Space Complexity: O(n) if you're using nums.sort(), or O(1) if you're using sorted(nums)
        '''
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

    def hasDuplicateHashSetLength(self, nums: list[int]) -> bool:
        '''
        We create a hashset from nums, and then compare its length to the length of nums.
        If the condition is true, that means that nums has duplicates. If the condition is false, that means that nums doesn't have duplicates
        Time Complexity: O(n) because of len()
        Space Complexity: O(n) because we are making a hashset from nums
        '''
        return len(set(nums)) != len(nums)
    
    

