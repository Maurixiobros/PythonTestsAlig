from typing import List

class Solution:
    def extractMaxYield(self, yields: List[int]) -> int:
        if not yields:
            return 0
        
        n = len(yields)
        
        # If there's only one asteroid, mine it
        if n == 1:
            return yields[0]
        
        # Initialize two variables to store the maximum yield up to the previous two positions
        prev2 = 0  # Maximum yield up to two positions before
        prev1 = 0  # Maximum yield up to the previous position
        
        for yield_value in yields:
            # Calculate the maximum yield for the current position
            current = max(prev1, prev2 + yield_value)
            
            # Update prev2 and prev1 for the next iteration
            prev2 = prev1
            prev1 = current
        
        return prev1

if __name__ == "__main__":
    # Read input from the user
    input_yields = list(map(int, input("Enter the yields separated by spaces: ").split()))
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Calculate and print the result
    print(solution.extractMaxYield(input_yields))