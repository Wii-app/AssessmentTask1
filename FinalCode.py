#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# Initialise the EV3 Brick
ev3 = EV3Brick()

# Initialise motors and sensors
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
gripper_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S2)

# Function to move the robot forward
def move_forward(speed, duration):
    left_motor.run(speed)
    right_motor.run(speed)
    wait(duration * 1000)  # Convert seconds to milliseconds
    stop_motors()

# Function to stop the motors
def stop_motors():
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

# unction to turn the robot
def turn(direction, duration):
    if direction == "left":
        left_motor.run(-200)
        right_motor.run(200)
    elif direction == "right":
        left_motor.run(200)
        right_motor.run(-200)
    wait(duration * 1000)  # Convert seconds to milliseconds
    stop_motors()

# Function to pick up a block
def pick_up_block():
    gripper_motor.run_time(500, 2000)  # Run at 500 deg/s for 2 seconds

# Function to drop a block
def drop_block():
    gripper_motor.run_time(-500, 2000)  # Run at -500 deg/s for 2 seconds

# Function to avoid obstacles
def avoid_obstacle():
    move_forward(-200, 1)  # Move backward
    turn("right", 1)       # Turn right

# Function to handle a block based on its color
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

# Move to the designated position
def move_to_designated_position():
    move_forward(200, 2)

# Main code
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

# Run the main program
if __name__ == "__main__":
    main()