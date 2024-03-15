import asyncio
import websockets
import serial
import re
from pijuice import PiJuice

# Initialize PiJuice and Serial for GSM HAT
pijuice = PiJuice(1, 0x14)
ser = serial.Serial('/dev/ttyUSB2', baudrate=115200, timeout=1)

def send_at_command(command, response_terminator=b'OK\r\n', wait_time=0.5):
    """Send an AT command to the GSM module and return its response."""
    ser.write(command.encode() + b'\r\n')
    asyncio.sleep(wait_time)  # Short pause to allow command processing
    response = ser.read_until(response_terminator).decode('utf-8', errors='ignore')
    return response.strip()

async def get_gps_coordinates():
    """Acquire GPS coordinates from the GSM module."""
    ser.write(b'AT+CGPS=1\r\n')
    await asyncio.sleep(120)  # Wait for GPS to acquire a signal

    ser.write(b'AT+CGPSINFO\r\n')
    response = ser.read_until(b'OK\r\n').decode('utf-8', errors='ignore')
    ser.write(b'AT+CGPS=0\r\n')  # Turn off GPS to save power

    match = re.search(r'\+CGPSINFO: .+,(.+),(.+),', response)
    if match:
        return match.groups()
    return None, None

async def battery_and_gps_status(websocket, path):
    """WebSocket service handling battery status, GPS coordinates, and AT command responses."""
    while True:
        try:
            message = await websocket.recv()  # Wait for a command from the client

            if message == "get_status":
                # Retrieve SIM and network status
                sim_status = send_at_command('AT+CPIN?')
                network_status = send_at_command('AT+CREG?')
                await websocket.send(f"SIM Status: {sim_status}, Network Status: {network_status}")
            else:
                # Get battery status
                status_data = pijuice.status.GetStatus()['data']
                charge_level = pijuice.status.GetChargeLevel()['data']
                charging_status = "Charging" if status_data['powerInput'] == 'PRESENT' or status_data['powerInput5vIo'] == 'PRESENT' else "Not Charging"

                # Get GPS coordinates
                latitude, longitude = await get_gps_coordinates()

                # Send battery and GPS status
                await websocket.send(f"Charging Status: {charging_status}, Charge Level: {charge_level}%, GPS: {latitude}, {longitude}")
                #await websocket.send(f"Charging Status: {charging_status}, Charge Level: {charge_level}%")

            await asyncio.sleep(60)  # Update interval
        except websockets.exceptions.ConnectionClosed:
            break

# ping all clients every 5 seconds to keep the connection alive
async def ping_clients():
    while True:
        await asyncio.sleep(5)
        await asyncio.wait([ws.ping() for ws in websockets.iter_websockets()])

start_server = websockets.serve(battery_and_gps_status, '0.0.0.0', 6789)


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
asyncio.ensure_future(ping_clients())