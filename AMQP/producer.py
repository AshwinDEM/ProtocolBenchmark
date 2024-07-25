import pika
import base64
import cv2
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
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Could not open webcam")
        return

    try:
        while not stop_event.is_set():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Encode the frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            encoded_string = base64.b64encode(buffer).decode('utf-8')

            # Send the encoded frame
            channel.basic_publish(exchange='',
                                  routing_key='video_queue',
                                  body=encoded_string)
    except KeyboardInterrupt:
        print(" [x] Stopped video streaming")
    finally:
        # Release the capture and close the connection
        cap.release()
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


