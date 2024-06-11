import asyncio
from aiocoap import *
import cv2
import base64

async def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    # Capture a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from webcam.")
        return

    # Encode the frame as a JPEG image
    ret, jpeg = cv2.imencode('.jpg', frame)
    if not ret:
        print("Error: Could not encode frame as JPEG.")
        return

    # Convert the encoded image to base64
    image_data = base64.b64encode(jpeg.tobytes()).decode('utf-8')

    # Create a CoAP context and send the base64 image data
    protocol = await Context.create_client_context()
    request = Message(code=POST, uri='coap://127.0.0.1/upload', payload=image_data.encode('utf-8'))

    try:
        response = await protocol.request(request).response
        print('Result: %s\n%r' % (response.code, response.payload))
    except Exception as e:
        print(f"Failed to send image: {e}")

    # Release the webcam
    cap.release()

if __name__ == "__main__":
    asyncio.run(main())
