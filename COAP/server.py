import asyncio
from aiocoap import *
from aiocoap.resource import Resource, Site
import base64

class CoAPServer(Resource):
    async def render_post(self, request):
        try:
            # Decode the base64-encoded image data
            image_data = base64.b64decode(request.payload)
            filename = 'received_image.jpg'
            with open(filename, 'wb') as f:
                f.write(image_data)
            print(f"Image saved as {filename}")
            return Message(code=CHANGED, payload=b'Image received')
        except Exception as e:
            print(f"Failed to save image: {e}")
            return Message(code=INTERNAL_SERVER_ERROR, payload=b'Failed to save image')

async def main():
    root = Site()
    root.add_resource(['upload'], CoAPServer())

    try:
        await Context.create_server_context(root, bind=('127.0.0.1', 5683))
        print("CoAP server is running on coap://127.0.0.1:5683/upload")
    except Exception as e:
        print(f"Failed to create CoAP server context: {e}")
        return

    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())
