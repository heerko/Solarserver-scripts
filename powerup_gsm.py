import RPi.GPIO as GPIO
import serial
import time
import os

# Define GPIO pin for power control and set up GPIO
power_key = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(power_key, GPIO.OUT)

def power_up():
    if not os.path.exists('/dev/ttyUSB2'):
        print('GSM HAT is not connected, cannot power up.')
        return

    print('Powering up the GSM HAT...')
    GPIO.output(power_key, GPIO.HIGH)
    time.sleep(2)  # Hold the power key high for 2 seconds to simulate a button press
    GPIO.output(power_key, GPIO.LOW)
    print('Waiting for GSM HAT to initialize...')
    time.sleep(20)  # Wait for the GSM HAT to initialize
    print('GSM HAT is powered on and ready.')


def initialize_serial():
    # Initialize serial connection to GSM HAT
    print("Initializing serial connection...")
    try:
        ser = serial.Serial('/dev/ttyUSB2', 115200, timeout=1)
        ser.flushInput()  # Clear the input buffer
        print("Serial connection established.")
        return ser
    except Exception as e:
        print(f"Failed to establish serial connection: {e}")
        return None

def send_at(ser, command, timeout=1):
    if ser:
        ser.write((command + '\r\n').encode())
        time.sleep(timeout)
        response = ser.read(ser.inWaiting()).decode()  # Read the response
        print(response)
        return response
    else:
        print("Serial connection not established. Cannot send AT command.")

# Power up the GSM HAT
power_up()

# Initialize serial connection after GSM HAT has booted
ser = initialize_serial()

# Example AT command to check network registration
send_at(ser, 'AT+CREG?')

# Cleanup
if ser:
    ser.close()
GPIO.cleanup()
