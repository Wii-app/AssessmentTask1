#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize a motor at port B.
test_motor = Motor(Port.B)

# Initialize motors and sensors
left_motor = LargeMotor(OUTPUT_A)
right_motor = LargeMotor(OUTPUT_B)
gripper_motor = MediumMotor(OUTPUT_C)
color_sensor = ColorSensor(INPUT_1)
ultrasonic_sensor = UltrasonicSensor(INPUT_2)

# Move forward to search for blocks
left_motor.on(30)
right_motor.on(30)
sleep(2)

# Stop and check for a block
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

# Move forward again
left_motor.on(30)
right_motor.on(30)
sleep(2)

# Stop and check for another block
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

# Avoid obstacles using the ultrasonic sensor
if ultrasonic_sensor.distance_centimeters < 10:
    left_motor.on(-30)
    right_motor.on(-30)
    sleep(1)
    left_motor.on(30)
    right_motor.on(-30)
    sleep(1)

# Move to the designated position
left_motor.on(30)
right_motor.on(30)
sleep(3)
left_motor.off()
right_motor.off()