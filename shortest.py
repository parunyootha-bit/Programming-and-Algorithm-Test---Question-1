import json


class ShortestWalker:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def get_straight_paths(self, start_val, end_val):
        paths = []
        starts = []

        # find all starting points
        for r in range(self.rows):
            for c in range(self.cols):
                if self.matrix[r][c] == start_val:
                    starts.append((r, c))
        
        # N, S, E, W
        directions = [
            (-1, 0, "N"), (1, 0, "S"), (0, 1, "E"), (0, -1, "W")
        ]

        for row_start, column_start in starts: #check each 2

            for dr, dc, move_name in directions: # loop through each direction
                current_values = [self.matrix[row_start][column_start]]
                
                r, c = row_start + dr, column_start + dc # move starting point in the direction
                
                while 0 <= r < self.rows and 0 <= c < self.cols: # go straight

                    val = self.matrix[r][c]
                    current_values.append(val) # get value for each step in the direction
                    
                    if val == end_val:
                        paths.append({
                            "direction": move_name,
                            "values": list(current_values) # The full sequence
                        })
                    
                    r += dr
                    c += dc
        
        return paths

    def display_results(self, start_val, end_val):

        results = self.get_straight_paths(start_val, end_val)
        
        if not results:
            print(f"NO ROUTE")
            return

        # sort each path by length (shortest first)
        results.sort(key=lambda x: len(x['values']))
        
        for i, p in enumerate(results):
            sequence_str = ",".join(map(str, p['values']))

            label = ""
            if i == 0:
                label = " SHORTEST"
            elif i == len(results) - 1:
                label = " LONGEST"

            print(f"{p['direction']} {sequence_str}{label}")


filename = "input1-3.txt"

try:
    with open(filename, 'r') as f:
        lines = f.readlines()
        
        matrix_data = json.loads(lines[0].strip())

        coords = json.loads(lines[1].strip())
        start_x, start_y = coords[0], coords[1]

    walker = ShortestWalker(matrix_data) 
    walker.display_results(start_x, start_y)

except FileNotFoundError:
    print("Error: File not found.")
except IndexError:
    print("Error: File is missing the second line for coordinates.")
except Exception as e:
    print(f"An error occurred: {e}")