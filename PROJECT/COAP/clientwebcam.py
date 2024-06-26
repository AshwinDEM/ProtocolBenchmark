import asyncio
from aiocoap import *
import base64
import imageio as iio

async def main():
    try:
        # Open the webcam
        camera = iio.get_reader("<video0>")
    except Exception as e:
        print(f"Error: Could not open video capture: {e}")
        return

    try:
        # Capture a frame from the webcam
        frame = camera.get_next_data()

        # Encode the frame as a JPEG image
        encoded_image = iio.imwrite('<bytes>', frame, format='jpg')

        # Convert the encoded image to base64
        image_data = base64.b64encode(encoded_image).decode('utf-8')

        # Create a CoAP context and send the base64 image data
        protocol = await Context.create_client_context()
        request = Message(code=POST, uri='coap://127.0.0.1/upload', payload=image_data.encode('utf-8'))

        try:
            response = await protocol.request(request).response
            print('Result: %s\n%r' % (response.code, response.payload))
        except Exception as e:
            print(f"Failed to send image: {e}")

    finally:
        # Release the webcam
        camera.close()

if __name__ == "__main__":
    asyncio.run(main())
