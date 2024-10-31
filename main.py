from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Step 1: Sort robots and factories
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)

        # Step 2: Dynamic programming approach
        dp = [float('inf')] * (n + 1)  # dp[i] will store the min distance for the first i robots
        dp[0] = 0  # No robot, no distance

        # Step 3: Process each factory
        for pos, limit in factory:
            # We need to traverse backwards to prevent overwriting dp[i] values that are still needed
            for k in range(n, -1, -1):
                # Try to take up to 'limit' robots from the previous dp state
                for j in range(1, limit + 1):
                    if k - j >= 0:  # Ensure we don't go out of bounds
                        # Calculate distance for these j robots going to the factory at 'pos'
                        dist = sum(abs(robot[k - x - 1] - pos) for x in range(j))
                        dp[k] = min(dp[k], dp[k - j] + dist)

        return dp[n]

# Example usage
sol = Solution()
robot1 = [0, 4, 6]
factory1 = [[2, 2], [6, 2]]
print(sol.minimumTotalDistance(robot1, factory1))  # Output: 4

robot2 = [1, -1]
factory2 = [[-2, 1], [2, 1]]
print(sol.minimumTotalDistance(robot2, factory2))  # Output: 2

