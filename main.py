#!/usr/bin/env python3
from time import sleep
from smbus import SMBus

from ev3dev2.display import Display
from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor import INPUT_1
from ev3dev2.port import LegoPort
from ev3dev2.button import Button

# Brick Variables
left_motor = LargeMotor(OUTPUT_D)
right_motor = LargeMotor(OUTPUT_A)

# Start program
target_duty_cycle = 75
correction_factor = 0.3
left_motor.duty_cycle_sp = target_duty_cycle
right_motor.duty_cycle_sp = target_duty_cycle
left_motor.run_direct()
right_motor.run_direct()

for i in range(100):
    left_degrees = left_motor.degrees
    right_degrees = right_motor.degrees
    steering = (left_degrees - right_degrees) * correction_factor

    left_duty = (target_duty_cycle - steering/2.0)
    if left_duty > 100:
        left_duty = 100
    elif left_duty < -100:
        left_duty = -100
    left_motor.duty_cycle_sp = left_duty

    right_duty = (target_duty_cycle + steering/2.0)
    if right_duty > 100:
        right_duty = 100
    elif right_duty < -100:
        right_duty = -100
    right_motor.duty_cycle_sp = right_duty

    sleep(0.1)

left_motor.stop()
right_motor.stop()
