import cv2
import paho.mqtt.client as mqtt
import base64
import signal
import sys

broker = 'localhost'  
port = 1883
topic = 'video'

def encode_frame(frame):
    _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    encoded_frame = base64.b64encode(buffer).decode('utf-8')
    return encoded_frame

client = mqtt.Client()
client.connect(broker, port, 60)

cap = cv2.VideoCapture(0)  

def signal_handler(sig, frame):
    print('Stopping video stream...')
    cap.release()
    cv2.destroyAllWindows()
    client.disconnect()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print('Press Ctrl+C to stop the video stream.')

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture video frame.")
        break
    
    encoded_frame = encode_frame(frame)
    client.publish(topic, encoded_frame)
    print("Published frame size:", len(encoded_frame))
    
    cv2.imshow('Video - Publisher', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
client.disconnect()
