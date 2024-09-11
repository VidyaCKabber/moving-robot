import constants
from robot import Robot


def main():
    # Initial input values (coordinates, commands)
    initial_x = int(input("Enter the initial row: "))
    initial_y = int(input("Enter the initial column: "))

    if initial_x < 0 or initial_y < 0 or initial_x > 4 or initial_y > 5:
        print("Invalid inputs: Grid dimentions are (4, 5). Please provide codinates in this range ")
        exit()

    initial_direction = input("Enter the initial direction (N, E, W, S): ").strip().upper()

    if initial_direction not in constants.DIRECTIONS:
        print(f"Invalid initial direction. Please provide valid direction in following {constants.DIRECTIONS}")
        exit()

    command = input("Enter the command string (e.g., 'MSMMEMM'): ").strip()

    # Locate robot's place at the given initial position and direction
    robot = Robot(constants.GRID_ROWS, constants.GRID_COLS, start_row=initial_x, start_col=initial_y, start_direction=initial_direction)

    robot.execute_commands(command)

    # Position of the robot after the command is executed
    print("\n Robot Current Location:", robot.get_position())

if __name__ == "__main__":
    main()
