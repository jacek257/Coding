'''
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of 3 instrutions:
    "G" for straight 1 unit
    "L" turn 90 degrees to the left
    "R" turn 90 degrees to the right
The robot performs the instrutions given in order and repeats forever
Return true if and only if the robot goes in a circle forever
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
                    # N      E       S        W
        direction = [[0,1], [1, 0], [0, -1], [-1, 0]]
        x = y = 0
        face = 0

        for move in instructions:
            if move == 'G':
                x += direction[face][0]
                y += direction[face][1]
            elif move == 'L':
                face = (face-1)%4
            else:
                face = (face+1)%4

        # if after one cycle and the robot returns to starting position, then any other cycle after will also return it to its starting position
        # if after 1 cycle and the robot is not facing north, then 3 cycles later, it will return the starting point facing north
        return (x == 0 and y == 0) or face != 0
