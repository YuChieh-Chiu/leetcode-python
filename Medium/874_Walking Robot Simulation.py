class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        Thought:
        - Goal: Find the maximum squared Euclidean distance the robot reaches after executing a sequence of commands while avoiding obstacles.
        - Idea: Simulate the robot's movement step-by-step. Since the maximum steps per command is small (up to 9), a step-by-step simulation is efficient. We can use a Hash Set to store obstacle coordinates, enabling O(1) lookup time to check for collisions during each step.
        - Steps:
            1. Initialize the robot's position at (0, 0), facing North, and set the maximum distance tracked to 0.
            2. Convert the list of obstacles into a Hash Set of tuples for constant-time lookups.
            3. Iterate through each command:
                - If it's a turning command (-1 or -2), update the current direction using modulo arithmetic.
                - If it's a moving command, move the robot one unit at a time in the current direction.
                - Before taking each step, check if the next coordinate exists in the obstacle set. If it does, stop moving for this command.
                - After executing the command (or stopping early), update the maximum squared distance reached so far.
            4. Return the maximum squared distance.
        - Time Complexity: O(N + M), where N is the length of commands and M is the length of obstacles. It takes O(M) to build the obstacle set, and O(N) to process commands (each move command takes at most 9 steps, which is O(1) constant time per command).
        - Space Complexity: O(M), where M is the length of obstacles, as we store all obstacle coordinates in a Hash Set.
    """
        x, y = 0, 0
        d = 1
        max_d = 0

        # 將 List[list] 轉換成 Set(tuple)
        o_set = {tuple(o) for o in obstacles}

        for c in commands:
            if c == -1:
                d = (d-1) % 4
            elif c == -2:
                d = (d+1) % 4
            else:
                for _ in range(c):
                    if d == 1: # north
                        y += 1
                        if (x,y) in o_set:
                            y -= 1
                            break
                    elif d == 2: # west
                        x -= 1
                        if (x,y) in o_set:
                            x += 1
                            break
                    elif d == 3: # south
                        y -= 1
                        if (x,y) in o_set:
                            y += 1
                            break
                    else: # east
                        x += 1
                        if (x,y) in o_set:
                            x -= 1
                            break
                max_d = max(x**2 + y**2, max_d)

        return max_d
