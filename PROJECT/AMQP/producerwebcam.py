import pika
import base64
import imageio as iio
import time
from threading import Event, Thread

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

    # Capture video from webcam
    try:
        camera = iio.get_reader("<video0>")
    except Exception as e:
        print(f"Could not open webcam: {e}")
        return

    meta = camera.get_meta_data()
    delay = 1 / meta["fps"]

    try:
        while not stop_event.is_set():
            frame = camera.get_next_data()
            
            # Encode the frame as JPEG
            encoded_image = iio.imwrite('<bytes>', frame, format='jpg')
            encoded_string = base64.b64encode(encoded_image).decode('utf-8')

            # Send the encoded frame
            channel.basic_publish(exchange='',
                                  routing_key='video_queue',
                                  body=encoded_string)
            
            time.sleep(delay)  # Control the frame rate
    except KeyboardInterrupt:
        print(" [x] Stopped video streaming")
    finally:
        # Release the capture and close the connection
        camera.close()
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
