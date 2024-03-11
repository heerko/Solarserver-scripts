import asyncio
import websockets.exceptions  # Import exceptions

async def get_status():
    uri = "ws://localhost:6789"  # Adjust as needed
    async with websockets.connect(uri) as websocket:
        await websocket.send("get_status")
        status_message = await websocket.recv()
        print(status_message)

if __name__ == "__main__":
    try:
        asyncio.run(get_status())
    except (OSError, websockets.exceptions.ConnectionClosedError) as e:
        print("Failed to connect or connection closed unexpectedly.")
