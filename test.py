import asyncio
import websockets

async def send_data():
    async with websockets.connect('ws://localhost:8765') as websocket:
        while True:
            message = input("Enter message to send: ")
            await websocket.send(message)
            print(f">>> Sent: {message}")
            greeting = await websocket.recv()
            print(f"<<< Received: {greeting}")

asyncio.run(send_data())