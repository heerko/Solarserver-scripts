import RPi.GPIO as GPIO
import time
import os

# Define GPIO pin for power control and set up GPIO
power_key = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(power_key, GPIO.OUT)

# Function to power down the GSM HAT if /dev/ttyUSB2 exists
def power_down():
    if os.path.exists('/dev/ttyUSB2'):
        print('Powering down the GSM HAT...')
        GPIO.output(power_key, GPIO.HIGH)
        time.sleep(3)  # Hold the power key high for 3 seconds to initiate shutdown
        GPIO.output(power_key, GPIO.LOW)
        print('GSM HAT is powered off.')
    else:
        print('GSM HAT is not active, no need to power down.')

# Execute the power down sequence
power_down()

# Cleanup GPIO resources
GPIO.cleanup()
