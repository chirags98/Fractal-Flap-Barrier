import RPi.GPIO as GPIO
import time

current_state = 0;


def relay_on(pin):
    global current_state
    GPIO.output(pin, GPIO.HIGH)  # Turn relay on
    current_state = 1


def relay_off(pin):
    global current_state
    GPIO.output(pin, GPIO.LOW)  # Turn relay off
    current_state = 0


def change_relay_state(pin):
    global current_state
    if current_state == 1:
        relay_off(pin)  # Turn relay off

    else:
        relay_on(pin)   # Turn relay off
