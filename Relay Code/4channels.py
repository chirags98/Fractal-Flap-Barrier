import relay as relay
import RPi.GPIO as GPIO
import time

channel1 = 16
channel2 = 20
channel3 = 21
channel4 = 26

# GPIO setup
GPIO.setmode(GPIO.BCM)

#Setup for channels
GPIO.setup(channel1, GPIO.OUT)
GPIO.setup(channel2, GPIO.OUT)
GPIO.setup(channel3, GPIO.OUT)
GPIO.setup(channel4, GPIO.OUT)
# Turn Relays off
relay.relay_off(channel1)
relay.relay_off(channel2)
relay.relay_off(channel3)
relay.relay_off(channel4)

if __name__ == '__main__':
    try:
        #Change state of relay
        relay.change_relay_state(channel3)
        print("Relay On \n")
        time.sleep(1)

        #Turn Relay off
        relay.relay_off(channel3)
        print("Relay Off \n")
        time.sleep(1)

        #Turn Relay on
        relay.relay_on(channel3)
        print("Relay On \n")
        time.sleep(1)

        # Change state of relay
        relay.change_relay_state(channel3)
        print("Relay Off \n")
        time.sleep(1)

        ######################################
        # Turn Relays on
        relay.relay_on(channel1)
        relay.relay_on(channel2)
        relay.relay_on(channel4)
        time.sleep(1)

        # Turn Relay off
        relay.relay_off(channel1)
        relay.relay_off(channel2)
        relay.relay_off(channel4)
        time.sleep(1)
        ######################################

        GPIO.cleanup()  #Call at the very end of the program (before exiting the program)
    except KeyboardInterrupt:
        GPIO.cleanup()  #Call at the very end of the program (before exiting the program)