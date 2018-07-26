import relay as relay
import RPi.GPIO as GPIO
import time

channel3 = 21

# GPIO setup
GPIO.setmode(GPIO.BCM)

#Setup for channels
GPIO.setup(channel3, GPIO.OUT)

if __name__ == '__main__':
    try:
        # Turn Relay off
        relay.relay_off(channel3)
        time.sleep(1)

        #Change state of relay
        relay.change_relay_state(channel3)
        time.sleep(1)

        #Turn Relay off
        relay.relay_off(channel3)
        time.sleep(1)

        #Turn Relay on
        relay.relay_on(channel3)
        time.sleep(1)

        # Change state of relay
        relay.change_relay_state(channel3)
        time.sleep(1)

        GPIO.cleanup()  #Call at the very end of the program (before exiting the program)
    except KeyboardInterrupt:
        GPIO.cleanup()  #Call at the very end of the program (before exiting the program)