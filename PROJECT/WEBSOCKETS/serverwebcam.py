# # SERVER
# # RECEIVES AND DISPLAYS WEBCAM VIDEO

# import asyncio
# import websockets
# import cv2
# import base64
# import numpy as np

# async def display_video(websocket, path):
#     async for message in websocket:
#         # print("Received frame")
#         img_data = base64.b64decode(message)
#         nparr = np.frombuffer(img_data, np.uint8)
#         frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#         cv2.imshow('Received Video', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit if 'q' is pressed
#             break

#     cv2.destroyAllWindows()

# async def main():
#     async with websockets.serve(display_video, "localhost", 8765):  # Use the server's IP address
#         await asyncio.Future()

# if __name__ == "__main__":
#     asyncio.run(main())

# SERVER
# RECEIVES AND DISPLAYS WEBCAM VIDEO USING MATPLOTLIB

import asyncio
import websockets
import base64
import numpy as np
import imageio as iio
import matplotlib.pyplot as plt

async def display_video(websocket, path):
    plt.ion()  # Interactive mode for live updating
    fig, ax = plt.subplots()

    async for message in websocket:
        print("Received frame")
        img_data = base64.b64decode(message)
        frame = iio.imread(img_data, format='jpg')

        ax.clear()
        ax.imshow(frame)
        plt.draw()
        plt.pause(0.001)


    plt.ioff()
    plt.show()

async def main():
    async with websockets.serve(display_video, "localhost", 8765):  # Use the server's IP address
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
