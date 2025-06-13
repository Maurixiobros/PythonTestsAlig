from typing import List

class Solution:
    def computeMaximumWindSurge(self, deviations: List[int]) -> int:
        # Initialize variables for Kadane's Algorithm
        max_current = deviations[0]  # Maximum sum of the current subarray
        max_global = deviations[0]  # Maximum sum found so far

        # Iterate through the array starting from the second element
        for i in range(1, len(deviations)):
            # Update the current maximum sum
            max_current = max(deviations[i], max_current + deviations[i])
            
            # Update the global maximum sum if the current sum is greater
            if max_current > max_global:
                max_global = max_current

        return max_global

# Input option
if __name__ == "__main__":
    # Read input from the user
    input_deviations = list(map(int, input("Enter the wind speed deviations separated by spaces: ").split()))
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Calculate and print the result
    print(solution.computeMaximumWindSurge(input_deviations))