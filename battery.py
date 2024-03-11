#!/usr/bin/python3
from pijuice import PiJuice

# Instantiate PiJuice interface object
pijuice = PiJuice(1, 0x14)

# Read PiJuice status.
status = pijuice.status.GetStatus()
charge_level_data = pijuice.status.GetChargeLevel()  # Get the charge level dictionary

# Extract the charge level value from the dictionary
charge_level = charge_level_data['data']

# Define a dictionary to map status values to human-readable strings
status_mapping = {
    'isFault': 'Fault Detected' if status['data']['isFault'] else 'No Fault',
    'isButton': 'Button Pressed' if status['data']['isButton'] else 'No Button Pressed',
    'battery': status['data']['battery'],
    'powerInput': status['data']['powerInput'],
    'powerInput5vIo': status['data']['powerInput5vIo']
}

# Print formatted status except for battery
print("PiJuice Status:")
print(f"- Fault Status: {status_mapping['isFault']}")
print(f"- Button Status: {status_mapping['isButton']}")
print(f"- Battery: {status_mapping['battery']}")
print(f"- Power Input: {status_mapping['powerInput']}")
print(f"- Power Input 5V IO: {status_mapping['powerInput5vIo']}")
print(f"- Charge Level: {charge_level}%")
