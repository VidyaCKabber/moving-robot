import constants

class Robot:
    def __init__(self, grid_rows, grid_cols, start_row, start_col, start_direction):
        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        self.x = start_row
        self.y = start_col
        self.direction = start_direction # N, E, W, S

    def turn(self, new_direction):
        '''
        Turn robot to the new direction if it's different from current direction
        '''
        if self.direction != new_direction:
            self.direction = new_direction

    def move(self):
        '''
        Move robot in the direction it's currently facing.

        For Example:
            1. Robot cannot move beyond the grid coordinates. 
               If it receives a command to move beyond the grid boundaries, it remains stationary.
               For eg: If current position of the grid is (3,0,S) and it receives ‘M’ instruction then 
                    it will not move as any movement south will cause it go out of the grid.

            2. If Robot gets an instruction to turn in a direction that it already facing, it will not take any action
               For eg: If robot is facing North and it gets an 'N' instruction, then it will not take any action
        '''
        
        if self.direction == 'N' and self.x > 0:
            self.x -= 1
        elif self.direction == 'S' and self.x < self.grid_rows - 1:
            self.x += 1
        elif self.direction == 'E' and self.y < self.grid_cols - 1:
            self.y += 1
        elif self.direction == 'W' and self.y > 0:
            self.y -= 1

    def execute_commands(self, commands):
        for command in commands:
            if command in constants.DIRECTIONS:
                self.turn(command)
            elif command == 'M':
                self.move()

    def get_position(self):
        return f"({self.x},{self.y},{self.direction})"