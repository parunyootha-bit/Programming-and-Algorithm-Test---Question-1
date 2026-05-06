import json


class ZigZagWalker:
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0


    @staticmethod
    def load_matrix_from_file(file_path):
        try:
            with open(file_path, 'r') as f:
                content = f.read().strip()
                return json.loads(content)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []        

    def gen_path(self):

        path = []
       
        for c in range(self.cols):
            column_values = []

            # loop through each column   
            for r in range(self.rows):
                value = self.matrix[r][c]
                column_values.append(value)
            
            # odd column reverse list
            if c % 2 != 0:
                column_values.reverse()
            
            path.extend(column_values)
            
        return path

    def run(self):

        for val in self.gen_path():
            print(f"{val}", sep="", end=",")

filename = "input1-1.txt"
loaded_data = ZigZagWalker.load_matrix_from_file(filename)

if loaded_data: 
    zigzag = ZigZagWalker(loaded_data)
    zigzag.run()
 