'''
Problem 4: Rubiks Cube Data Structure
- Each face can be represented by a 2D array where each element corresponds to a tile on that face
- 6 faces: front, back, left, right, top, and bottom
- N is the size of the cube
- Represent the cube as a dictionary where the keys are the face names and the values are 2D arrays 
  representing the tiles

Layer Rotation:
- Should be able to manipulate both the tiles on the rotating face and the tiles of the adjacent faces
- In order to rotate the 2D array the program should transpose the matrix then reverse rows or columns
- This also needs to apply to the adjacent faces that are affected by the rotation. 
- Need two methods of rotation:
    - rotate face
    - rotate layer
'''

class RubiksCube:
    def __init__(self, size=3):
        self.size = size
        self.cube = {
            'U': [['R'] * size for _ in range(size)],  # Up (Red)
            'D': [['B'] * size for _ in range(size)],  # Down (Blue)
            'F': [['G'] * size for _ in range(size)],  # Front (Green)
            'B': [['O'] * size for _ in range(size)],  # Back (Orange)
            'L': [['W'] * size for _ in range(size)],  # Left (White)
            'R': [['Y'] * size for _ in range(size)]   # Right (Yellow)
        }
    
    def display(self):
        """Display the cube's current state"""
        for face, grid in self.cube.items():
            print(f"{face} face:")
            for row in grid:
                print(" ".join(row))
            print()

    def rotate_face(self, face, clockwise=True):
        """Rotates a single face and updates the adjacent layers"""
        self.cube[face] = self.rotate_grid(self.cube[face], clockwise)

        if face == 'F':
            self.rotate_edges_front(clockwise)
        elif face == 'B':
            self.rotate_edges_back(clockwise)
        elif face == 'U':
            self.rotate_edges_up(clockwise)
        elif face == 'D':
            self.rotate_edges_down(clockwise)
        elif face == 'L':
            self.rotate_edges_left(clockwise)
        elif face == 'R':
            self.rotate_edges_right(clockwise)
    
    def rotate_grid(self, grid, clockwise=True):
        """Rotate a 2D grid 90 degrees"""
        if clockwise:
            return [list(reversed(col)) for col in zip(*grid)]
        else:
            return [list(col) for col in reversed(list(zip(*grid)))]
    
    def rotate_edges_front(self, clockwise):
        """Updates the adjacent layers when rotating the front face"""
        top_row = self.cube['U'][-1][:]
        left_col = [self.cube['L'][i][-1] for i in range(self.size)] 
        bottom_row = self.cube['D'][0][:] 
        right_col = [self.cube['R'][i][0] for i in range(self.size)] 
        
        if clockwise:
            # Update Up -> Right -> Down -> Left -> Up
            self.cube['U'][-1] = left_col[::-1]
            for i in range(self.size):
                self.cube['L'][i][-1] = bottom_row[i]
            self.cube['D'][0] = right_col[::-1]
            for i in range(self.size):
                self.cube['R'][i][0] = top_row[i]
        else:
            self.cube['U'][-1] = right_col
            for i in range(self.size):
                self.cube['R'][i][0] = bottom_row[::-1][i]
            self.cube['D'][0] = left_col
            for i in range(self.size):
                self.cube['L'][i][-1] = top_row[::-1][i]

    def rotate_edges_back(self, clockwise):
        """Updates the adjacent layers when rotating the back face"""
        top_row = self.cube['U'][0][:]  
        left_col = [self.cube['L'][i][0] for i in range(self.size)] 
        bottom_row = self.cube['D'][-1][:]  
        right_col = [self.cube['R'][i][-1] for i in range(self.size)] 

        if clockwise:
            # Update Up -> Left -> Down -> Right -> Up (Back rotation affects opposite edges)
            self.cube['U'][0] = right_col
            for i in range(self.size):
                self.cube['R'][i][-1] = bottom_row[::-1][i]
            self.cube['D'][-1] = left_col
            for i in range(self.size):
                self.cube['L'][i][0] = top_row[::-1][i]
        else:
            # Counterclockwise
            self.cube['U'][0] = left_col[::-1]
            for i in range(self.size):
                self.cube['L'][i][0] = bottom_row[i]
            self.cube['D'][-1] = right_col[::-1]
            for i in range(self.size):
                self.cube['R'][i][-1] = top_row[i]

    def rotate_edges_up(self, clockwise):
        """Updates the adjacent layers when rotating the up face"""
        front_row = self.cube['F'][0][:] 
        right_row = self.cube['R'][0][:]  
        back_row = self.cube['B'][0][:]  
        left_row = self.cube['L'][0][:]  

        if clockwise:
            # Rotate Front -> Right -> Back -> Left -> Front
            self.cube['F'][0] = left_row
            self.cube['R'][0] = front_row
            self.cube['B'][0] = right_row
            self.cube['L'][0] = back_row
        else:
            # Counterclockwise
            self.cube['F'][0] = right_row
            self.cube['R'][0] = back_row
            self.cube['B'][0] = left_row
            self.cube['L'][0] = front_row

    def rotate_edges_down(self, clockwise):
        """Updates the adjacent layers when rotating the down face"""
        front_row = self.cube['F'][-1][:]  
        right_row = self.cube['R'][-1][:]  
        back_row = self.cube['B'][-1][:]  
        left_row = self.cube['L'][-1][:]  

        if clockwise:
            # Rotate Front -> Right -> Back -> Left -> Front
            self.cube['F'][-1] = left_row
            self.cube['R'][-1] = front_row
            self.cube['B'][-1] = right_row
            self.cube['L'][-1] = back_row
        else:
            # Counterclockwise
            self.cube['F'][-1] = right_row
            self.cube['R'][-1] = back_row
            self.cube['B'][-1] = left_row
            self.cube['L'][-1] = front_row

    def rotate_edges_left(self, clockwise):
        """Updates the adjacent layers when rotating the left face"""
        front_col = [self.cube['F'][i][0] for i in range(self.size)] 
        up_col = [self.cube['U'][i][0] for i in range(self.size)]  
        back_col = [self.cube['B'][i][-1] for i in range(self.size)]  
        down_col = [self.cube['D'][i][0] for i in range(self.size)] 

        if clockwise:
            # Rotate Front -> Up -> Back -> Down -> Front
            for i in range(self.size):
                self.cube['F'][i][0] = down_col[i]
                self.cube['U'][i][0] = front_col[i]
                self.cube['B'][i][-1] = up_col[::-1][i]
                self.cube['D'][i][0] = back_col[::-1][i]
        else:
            # Counterclockwise
            for i in range(self.size):
                self.cube['F'][i][0] = up_col[i]
                self.cube['U'][i][0] = back_col[::-1][i]
                self.cube['B'][i][-1] = down_col[i]
                self.cube['D'][i][0] = front_col[i]

    def rotate_edges_right(self, clockwise):
        """Updates the adjacent layers when rotating the right face"""
        front_col = [self.cube['F'][i][-1] for i in range(self.size)] 
        up_col = [self.cube['U'][i][-1] for i in range(self.size)]  
        back_col = [self.cube['B'][i][0] for i in range(self.size)]  
        down_col = [self.cube['D'][i][-1] for i in range(self.size)]  

        if clockwise:
            # Rotate Front -> Up -> Back -> Down -> Front
            for i in range(self.size):
                self.cube['F'][i][-1] = down_col[i]
                self.cube['U'][i][-1] = front_col[i]
                self.cube['B'][i][0] = up_col[::-1][i]
                self.cube['D'][i][-1] = back_col[::-1][i]
        else:
            # Counterclockwise
            for i in range(self.size):
                self.cube['F'][i][-1] = up_col[i]
                self.cube['U'][i][-1] = back_col[::-1][i]
                self.cube['B'][i][0] = down_col[i]
                self.cube['D'][i][-1] = front_col[i]


# Tests
print("Cube 1:\n")
cube = RubiksCube(2)
cube.display()
cube.rotate_face('F')  # Rotate front face clockwise
cube.display()

print("Cube 2:\n")
cube2 = RubiksCube(3)
cube2.display()
cube2.rotate_face('U', clockwise=False)
cube2.display()
