import asyncio
import websockets
import base64
import numpy as np
import cv2

async def save_video(websocket, path):
    output_file = 'received_video2.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))  # Adjust frame size if needed

    try:
        async for message in websocket:
            print("Received frame")
            img_data = base64.b64decode(message)
            nparr = np.frombuffer(img_data, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Write frame to video file
            writer.write(frame)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        writer.release()
        print(f"Video saved as {output_file}")

async def main():
    async with websockets.serve(save_video, "172.20.10.3", 8765):  # Use the server's IP address
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
