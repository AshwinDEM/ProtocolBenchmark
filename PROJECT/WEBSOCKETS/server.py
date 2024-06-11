# SERVER
# RECEIVES DATA

import asyncio
import websockets
import cv2
import base64
import numpy as np

async def echo(websocket, path):
    async for message in websocket:
        print("Received message")
        img_data = base64.b64decode(message)
        nparr = np.frombuffer(img_data, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imshow('Received Image', img_np)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # await websocket.send("Message received!")

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())