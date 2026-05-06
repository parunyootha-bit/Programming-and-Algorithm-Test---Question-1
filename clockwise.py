import json


class ClockwiseWalker:
    def __init__(self, matrix):
        self.matrix = matrix
        self.max_rows = len(matrix)
        self.max_cols = len(matrix[0]) if self.max_rows > 0 else 0

    def get_path(self, start_x, start_y):
        path = []

        # starting point 1,1      
        top = start_y # top-most
        left = 0 # left-most 
        
        # boundaries of the current box to walk around  6-1, 7-1            
        bottom = self.max_rows - 1
        right = self.max_cols - 1

        first_run = True

        # While we have a valid box to walk around
        # if start 1,1
        # first loop 1,1 - 1,6 - 5,6 - 5,0 - 2,0
        # next loop 2,1 - 2,5 - 4,5 - 4,1 - 3,1
        # next loop 3,2 - 3,4
        while top <= bottom and left <= right:

            current_start_x = start_x if first_run else left # use this to go left-most on first run
            
            # go right first (1 , 7) 
            for i in range(current_start_x, right + 1):  
                path.append(self.matrix[top][i])
            top += 1 # move top down

            # then go down  (2 , 6)           
            for i in range(top, bottom + 1): 
                path.append(self.matrix[i][right]) 
            right -= 1 # move right closer 

            # then go left
            if top <= bottom: # check if near center or not

                # count backwards from right to left (5 to 0)
                for i in range(right, left - 1, -1):
                    path.append(self.matrix[bottom][i])
                bottom -= 1 # move botom up 

            # then go up but not further than top
            if left <= right: # check if near center or not

                # count backwards from bottom to top (4 to 0)
                for i in range(bottom, top - 1, -1):
                    path.append(self.matrix[i][left]) 
                left += 1 # move left closer
            
            first_run = False

        return path

filename = "input1-2.txt"

try:
    with open(filename, 'r') as f:
        lines = f.readlines()
        
        matrix_data = json.loads(lines[0].strip())

        coords = json.loads(lines[1].strip())
        start_x, start_y = coords[0], coords[1]

    walker = ClockwiseWalker(matrix_data) 
    result_path = walker.get_path(start_x, start_y)

    for val in result_path:
        print(f"{val}", sep="", end=",")

except FileNotFoundError:
    print("Error: File not found.")
except IndexError:
    print("Error: File is missing the second line for coordinates.")
except Exception as e:
    print(f"An error occurred: {e}")