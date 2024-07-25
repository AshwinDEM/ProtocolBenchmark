# import asyncio
# import websockets
# import base64
# import time
# import picamera
# import picamera.array

# async def send_video(uri):
#     try:
#         async with websockets.connect(uri) as websocket:
#             with picamera.PiCamera() as camera:
#                 camera.resolution = (640, 480)
#                 camera.framerate = 30

#                 with picamera.array.PiRGBArray(camera, size=(640, 480)) as stream:
#                     for frame in camera.capture_continuous(stream, format='bgr', use_video_port=True):
#                         image = frame.array

#                         # Encode the frame as JPEG
#                         encoded_image = cv2.imencode('.jpg', image)[1].tobytes()
#                         jpg_as_text = base64.b64encode(encoded_image).decode('utf-8')

#                         # Send the frame
#                         await websocket.send(jpg_as_text)

#                         # Uncomment below to receive response from server
#                         # response = await websocket.recv()
#                         # print(f"Received response: {response}")

#                         stream.truncate(0)  # Reset the stream for the next frame

#                         time.sleep(0.033)  # Control the frame rate

#     except ConnectionRefusedError:
#         print(f"Could not connect to WebSocket server at {uri}.")

# if __name__ == "__main__":
#     uri = "ws://172.20.10.2:8765"  # Use the server's IP address
#     asyncio.run(send_video(uri))


import asyncio
import websockets
import base64
import time
import picamera
import picamera.array
from PIL import Image
from io import BytesIO

async def send_video(uri):
    try:
        async with websockets.connect(uri) as websocket:
            with picamera.PiCamera() as camera:
                camera.resolution = (640, 480)
                camera.framerate = 30

                with picamera.array.PiRGBArray(camera, size=(640, 480)) as stream:
                    for frame in camera.capture_continuous(stream, format='rgb', use_video_port=True):
                        image = frame.array

                        # Convert the image to a PIL Image
                        pil_image = Image.fromarray(image)
                        
                        # Encode the frame as JPEG using Pillow
                        buffered = BytesIO()
                        pil_image.save(buffered, format="JPEG")
                        encoded_image = buffered.getvalue()
                        jpg_as_text = base64.b64encode(encoded_image).decode('utf-8')

                        # Send the frame
                        await websocket.send(jpg_as_text)

                        # Uncomment below to receive response from server
                        # response = await websocket.recv()
                        # print(f"Received response: {response}")

                        stream.truncate(0)  # Reset the stream for the next frame

                        time.sleep(0.033)  # Control the frame rate

    except ConnectionRefusedError:
        print(f"Could not connect to WebSocket server at {uri}.")

if __name__ == "__main__":
    uri = "ws://172.20.10.2:8765"  # Use the server's IP address
    asyncio.run(send_video(uri))
