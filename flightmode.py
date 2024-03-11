import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setup(4, GPIO.OUT)  # P7 is BCM P4

# Enable flight mode
GPIO.output(4, GPIO.HIGH)  # Pull P7 (BCM P4) high
time.sleep(30)
GPIO.output(4, GPIO.LOW)
