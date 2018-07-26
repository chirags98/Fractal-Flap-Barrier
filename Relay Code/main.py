import relay.py as relay
import RPi.GPIO as GPIO
import time

channel = 21

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

if __name__ == '__main__':
    try:
        relay.relay_on(channel)
        time.sleep(1)
        relay.relay_off(channel)
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()