#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize motors and sensors
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
gripper_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S2)

# Function to move forward for a specified duration
def move_forward(speed, duration):
    left_motor.run(speed)
    right_motor.run(speed)
    wait(duration * 1000)  # Convert seconds to milliseconds
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

# Function to turn the robot
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

# Main program loop
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

# Final move to the designated position
move_forward(200, 3)