# # CLIENT
# # STREAMS WEBCAM VIDEO

# import asyncio
# import websockets
# import base64
# import cv2

# async def send_video(uri):
#     try:
#         async with websockets.connect(uri) as websocket:
#             cap = cv2.VideoCapture(0)  # Open the webcam

#             while True:
#                 ret, frame = cap.read()  # Capture frame-by-frame
#                 if not ret:
#                     print("Failed to capture image")
#                     break

#                 # Encode the frame as JPEG
#                 _, buffer = cv2.imencode('.jpg', frame)
#                 # Encode the buffer as base64
#                 jpg_as_text = base64.b64encode(buffer).decode('utf-8')

                
                
#                 # Send the frame
#                 await websocket.send(jpg_as_text)

#                 # response = await websocket.recv()
#                 # print(f"Received response: {response}")

#                 await asyncio.sleep(0.1)  # Adjust the sleep time as needed

#             cap.release()
#     except ConnectionRefusedError:
#         print(f"Could not connect to WebSocket server at {uri}.")

# if __name__ == "__main__":
#     uri = "ws://localhost:8765"  # Use the server's IP address
#     asyncio.run(send_video(uri))

# CLIENT
# STREAMS WEBCAM VIDEO USING IMAGEIO

import asyncio
import websockets
import base64
import imageio as iio
import time

async def send_video(uri):
    try:
        async with websockets.connect(uri) as websocket:
            camera = iio.get_reader("<video0>")  # Open the webcam
            meta = camera.get_meta_data()
            delay = 2 / meta["fps"]

            while True:
                frame = camera.get_next_data()  # Capture frame-by-frame

                # Encode the frame as JPEG
                encoded_image = iio.imwrite('<bytes>', frame, format='jpg')
                jpg_as_text = base64.b64encode(encoded_image).decode('utf-8')

                # Send the frame
                await websocket.send(jpg_as_text)

                # Uncomment below to receive response from server
                # response = await websocket.recv()
                # print(f"Received response: {response}")

                time.sleep(delay)  # Control the frame rate

            camera.close()
    except ConnectionRefusedError:
        print(f"Could not connect to WebSocket server at {uri}.")

if __name__ == "__main__":
    uri = "ws://localhost:8765"  # Use the server's IP address
    asyncio.run(send_video(uri))
