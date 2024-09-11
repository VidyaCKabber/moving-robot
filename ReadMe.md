Let me explain how this scripts for following sample input

For example:
Initial location (3, 2), and the robot is facing North (N).
command -> MEMTMMSMW

1. Robot's Initial location
   Grid size: 5 columns and 4 rows (0-indexed).
   Initial position: (3, 2) and facing North (N).

2. Command is MEMTMMSMW, let's solve this step by step
   a. Inital command is 'M' -> The robot is facing North (N), so it moves one step up i.e (3, 2) -> (2, 2)

   b. Next command is 'E' -> The robot turns to face East (E) and position remains the same at (2,2).

   c. Next command is 'M' -> The robot is facing East (E), so it moves one step to the right. New location is, (2,3)

   d. Next command is 'T' -> T is not a valid command, the robot will ignore this command and stay at (2,3,E)

   e. Next command is 'M' -> The robot is facing East (E), so it moves one step to the right i.e (2,3) -> (2,4)

   f. Next command is 'M' -> The robot is facing East (E), however the grid boundary is 4, hence the robot stays at (2,4) and does not move.

   g. Next command is 'S' -> The robot turns to face South (S) and position remains same i.e (2,4)

   h. Next command is 'M' -> The robot is facing South, move towards down. New position is (3,4)

   i. Last command is 'W' -> The robot is facing West (W), and location remains same (3,4)

3. Position of the robot after the command is executed is (3,4,W)
