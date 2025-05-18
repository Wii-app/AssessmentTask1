# Testing and Debugging

## Test Case 1
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

#Initialise the EV3 Brick.
ev3 = EV3Brick()

#Initialise a motor at port B.
test_motor = Motor(Port.B)

#Initialise motors and sensors
left_motor = LargeMotor(OUTPUT_A)
right_motor = LargeMotor(OUTPUT_B)
gripper_motor = MediumMotor(OUTPUT_C)
color_sensor = ColorSensor(INPUT_1)
ultrasonic_sensor = UltrasonicSensor(INPUT_2)

#Move forward to search for blocks
left_motor.on(30)
right_motor.on(30)
sleep(2)

#Stop and check for a block
left_motor.off()
right_motor.off()
if color_sensor.color == ColorSensor.COLOR_RED:
    # Pick up the red block
    gripper_motor.on_for_seconds(50, 2)
    left_motor.on(30)
    right_motor.on(30)
    sleep(2)
    left_motor.off()
    right_motor.off()
    gripper_motor.on_for_seconds(-50, 2)  # Drop the block

#Move forward again
left_motor.on(30)
right_motor.on(30)
sleep(2)

#Stop and check for another block
left_motor.off()
right_motor.off()
if color_sensor.color == ColorSensor.COLOR_YELLOW:
    # Pick up the yellow block
    gripper_motor.on_for_seconds(50, 2)
    left_motor.on(30)
    right_motor.on(30)
    sleep(2)
    left_motor.off()
    right_motor.off()
    gripper_motor.on_for_seconds(-50, 2)  # Drop the block

#Avoid obstacles using the ultrasonic sensor
if ultrasonic_sensor.distance_centimeters < 10:
    left_motor.on(-30)
    right_motor.on(-30)
    sleep(1)
    left_motor.on(30)
    right_motor.on(-30)
    sleep(1)

#Move to the designated position
left_motor.on(30)
right_motor.on(30)
sleep(3)
left_motor.off()
right_motor.off()


## Test Case 1 - Evaluation
The provided code for the LEGO EV3 robot introduces functionality for autonomous mobility, block detection, and obstacle 
avoidance. It utilises two large motors for locomotion, a medium motor for gripping, a colour sensor for identifying red and 
yellow blocks, and an ultrasonic sensor for obstacle detection. The robot moves forward, stops to look for blocks, grabs red 
or yellow blocks, and drops them off at certain points. Obstacle avoidance is attempted by reversing and turning when an 
objects detected at 10 cm. The code suffers from numerous drawbacks like hardcoded sleep values, and poor error handling.
Mixing pybricks and ev3dev2 libraries creates compatibility issues, and the obstacle detection threshold is too low for 
successful avoidance. While functional, the code can be improved by changing repetitive tasks into functions, increasing the 
range of obstacle detection, and adding error handling for unrecognised colours or sensor failure.


## Test Case 2
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

#Initialise the EV3 Brick
ev3 = EV3Brick()

#Initialise motors and sensors
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
gripper_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S2)

#Function to move forward for a specified duration
def move_forward(speed, duration):
    left_motor.run(speed)
    right_motor.run(speed)
    wait(duration * 1000)  # Convert seconds to milliseconds
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

#Function to turn the robot
def turn(direction, duration):
    if direction == "left":
        left_motor.run(-200)
        right_motor.run(200)
    elif direction == "right":
        left_motor.run(200)
        right_motor.run(-200)
    wait(duration * 1000)  # Convert seconds to milliseconds
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

#Function to pick up a block
def pick_up_block():
    gripper_motor.run_time(500, 2000)  # Run at 500 deg/s for 2 seconds

#Function to drop a block
def drop_block():
    gripper_motor.run_time(-500, 2000)  # Run at -500 deg/s for 2 seconds

#Function to avoid obstacles
def avoid_obstacle():
    move_forward(-200, 1)  # Move backward
    turn("right", 1)       # Turn right

#Main program loop
for _ in range(2):  # Repeat for two blocks (red and yellow)
    move_forward(200, 2)  # Move forward to search for blocks

    # Check for a block
    detected_color = color_sensor.color()
    if detected_color == ColorSensor.COLOR_RED:
        pick_up_block()
        move_forward(200, 2)  # Move to the designated position
        drop_block()
    elif detected_color == ColorSensor.COLOR_YELLOW:
        pick_up_block()
        move_forward(200, 2)  # Move to the designated position
        drop_block()

    # Check for obstacles
    if ultrasonic_sensor.distance() < 200:  # Distance in millimeters
        avoid_obstacle()

#Final move to the designated position
move_forward(200, 3)


## Test Case 2 - Evaluation
The 2nd code demonstrates a good example implementation for a LEGO EV3 robot using the pybricks library compared with the 
first code. It can move, turn, block pickup, and block drop functionalities as well as obstacle detection. The robot uses a
colour sensor to detect red and yellow blocks and ultrasonic for obstacles detection. There are areas for improvement. First,
the colour sensor method might return None when no colour is detected, which is not addressed in the code and can result in 
runtime exceptions. Probing for None or incorrect colours would improve robustness. Second, the hardcoded speeds and turn 
times for moving and turning may fail in all situations; these might be set dynamically based on sensor feedback or 
environment. Such changes would make the program more robust, efficient, and relevant to real-world applications.


## Final Test Case
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

#Initialise the EV3 Brick
ev3 = EV3Brick()

#Initialise motors and sensors
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
gripper_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S2)

#Function to move the robot forward
def move_forward(speed, duration):
    left_motor.run(speed)
    right_motor.run(speed)
    wait(duration * 1000)  # Convert seconds to milliseconds
    stop_motors()

#Function to stop the motors
def stop_motors():
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

#Function to turn the robot
def turn(direction, duration):
    if direction == "left":
        left_motor.run(-200)
        right_motor.run(200)
    elif direction == "right":
        left_motor.run(200)
        right_motor.run(-200)
    wait(duration * 1000)  # Convert seconds to milliseconds
    stop_motors()

#Function to pick up a block
def pick_up_block():
    gripper_motor.run_time(500, 2000)  # Run at 500 deg/s for 2 seconds

#Function to drop a block
def drop_block():
    gripper_motor.run_time(-500, 2000)  # Run at -500 deg/s for 2 seconds

#Function to avoid obstacles
def avoid_obstacle():
    move_forward(-200, 1)  # Move backward
    turn("right", 1)       # Turn right

#Function to handle a block based on its color
def handle_block(color):
    if color == ColorSensor.COLOR_RED:

        ev3.screen.print("Red block detected!")
        pick_up_block()
        move_to_designated_position()
        drop_block()
    elif color == ColorSensor.COLOR_YELLOW:
        ev3.screen.print("Yellow block detected!")
        pick_up_block()
        move_to_designated_position()
        drop_block()

#Move to the designated position
def move_to_designated_position():
    move_forward(200, 2)

#Main code
def main():
    blocks_to_collect = 2  # Number of blocks to collect (red and yellow)
    collected_blocks = 0

    while collected_blocks < blocks_to_collect:
        move_forward(200, 2)  # Move forward to search for blocks

        # Check for a block
        detected_color = color_sensor.color()
        if detected_color is not None and detected_color in [ColorSensor.COLOR_RED, ColorSensor.COLOR_YELLOW]:
            handle_block(detected_color)
            collected_blocks += 1
        else:
            ev3.screen.print("No valid block detected.")

        # Check for obstacles
        if ultrasonic_sensor.distance() < 200:  # Distance in millimeters
            ev3.screen.print("Obstacle detected!")
            avoid_obstacle()

    # Final move to the designated position
    move_forward(200, 3)
    ev3.screen.print("Task completed!")

#Run the main program
if __name__ == "__main__":
    main()


## Final Test Case - Evaluation
This script is working correctly and is performing as it should. It runs a LEGO EV3 robot that can move, search for blocks 
based on a colour sensor, and prevent collisions based on an ultrasonic sensor. The robot can search for red and yellow 
blocks, pick them up with a gripper motor, and transport them to a specific area. The code itself is extremely well structured 
and written, with different sections for movement, turning, block picking, and obstacle avoidance. This not only makes it easy 
to read but also to modify if needed. It also shows messages on the EV3 screen, which is useful as you can see what the robot 
is running. Overall, the code works, uses sensors well such as colour and ultra sensors. My code wasn't used for the final 
group code due to my friends unable to understand what is going on in the code. My group decided on another friend's code that 
is simple and easy to understand for ny group.