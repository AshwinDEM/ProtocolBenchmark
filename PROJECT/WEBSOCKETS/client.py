# CLIENT
# SENDS DATA

import asyncio
import websockets
import base64

def get_base64_encoded_image(image_path) -> str:
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"File {image_path} not found.")
        return None
    
def get_base64_encoded_video(video_path) -> str:
    try:
        with open(video_path, "rb") as video_file:
            return base64.b64encode(video_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"File {video_path} not found.")
        return None

async def send_message():
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            message = get_base64_encoded_image("image.jpg")
            if message is not None:
                print(f"Sending message: {message}")
                await websocket.send(message)
                
                # response = await websocket.recv()
                # print(f"Received response: {response}")
    except ConnectionRefusedError:
        print("Could not connect to WebSocket server at {uri}.")

if __name__ == "__main__":
    asyncio.run(send_message())