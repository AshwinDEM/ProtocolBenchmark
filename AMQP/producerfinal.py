import pika
import base64
import time
from threading import Event, Thread
import picamera
import picamera.array
from PIL import Image
from io import BytesIO

def send_message():
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='hello')

    # Prompt the user for the message
    message = input("Enter the message to be sent: ")

    # Send the message
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    print(f" [x] Sent message: '{message}'")

    # Close the connection
    connection.close()

def send_video(stop_event):
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='video_queue')

    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 30

        with picamera.array.PiRGBArray(camera, size=(640, 480)) as stream:
            try:
                while not stop_event.is_set():
                    camera.capture(stream, format='rgb', use_video_port=True)
                    image = stream.array

                    # Convert the image to a PIL Image
                    pil_image = Image.fromarray(image)

                    # Encode the frame as JPEG using Pillow
                    buffered = BytesIO()
                    pil_image.save(buffered, format="JPEG")
                    encoded_image = buffered.getvalue()
                    encoded_string = base64.b64encode(encoded_image).decode('utf-8')

                    # Send the encoded frame
                    channel.basic_publish(exchange='',
                                          routing_key='video_queue',
                                          body=encoded_string)

                    stream.truncate(0)  # Reset the stream for the next frame

                    time.sleep(0.033)  # Control the frame rate
            except KeyboardInterrupt:
                print(" [x] Stopped video streaming")
            finally:
                # Release the capture and close the connection
                connection.close()

if __name__ == "__main__":
    choice = input("Enter 'm' to send a message or 'v' to stream video from webcam: ")
    if choice == 'm':
        send_message()
    elif choice == 'v':
        stop_event = Event()
        video_thread = Thread(target=send_video, args=(stop_event,))
        video_thread.start()

        input("Press Enter to stop streaming...\n")
        stop_event.set()
        video_thread.join()
    else:
        print("Invalid choice")
