import paho.mqtt.client as mqtt
import base64
import signal
import sys
from picamera import PiCamera
from picamera.array import PiRGBArray
from PIL import Image
import io

broker = 'localhost'  
port = 1883
topic = 'video'

def encode_frame(frame):
    # Convert the frame to a PIL image
    image = Image.fromarray(frame)
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG', quality=90)
    encoded_frame = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return encoded_frame

client = mqtt.Client()
client.connect(broker, port, 60)

camera = PiCamera()
camera.resolution = (640, 480)
raw_capture = PiRGBArray(camera, size=(640, 480))

def signal_handler(sig, frame):
    print('Stopping video stream...')
    camera.close()
    client.disconnect()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print('Press Ctrl+C to stop the video stream.')

for frame in camera.capture_continuous(raw_capture, format='bgr', use_video_port=True):
    image = frame.array
    encoded_frame = encode_frame(image)
    client.publish(topic, encoded_frame)
    print("Published frame size:", len(encoded_frame))
    
    raw_capture.truncate(0)  # Clear the stream for the next frame

    # Display the frame (optional)
    image.show()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.close()
client.disconnect()
