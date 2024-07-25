import asyncio
from aiocoap import *
import base64
from picamera import PiCamera
from io import BytesIO
from PIL import Image

async def main():
    # Initialize the camera
    camera = PiCamera()
    camera.resolution = (640, 480)

    try:
        # Capture a frame from the webcam
        stream = BytesIO()
        camera.capture(stream, format='jpeg')
        stream.seek(0)
        image = Image.open(stream)

        # Convert the image to base64
        buffer = BytesIO()
        image.save(buffer, format='JPEG')
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Create a CoAP context and send the base64 image data
        protocol = await Context.create_client_context()
        request = Message(code=POST, uri='coap://172.20.10.2/upload', payload=image_data.encode('utf-8'))

        try:
            response = await protocol.request(request).response
            print('Result: %s\n%r' % (response.code, response.payload))
        except Exception as e:
            print(f"Failed to send image: {e}")

    finally:
        # Release the camera
        camera.close()

if __name__ == "__main__":
    asyncio.run(main())
