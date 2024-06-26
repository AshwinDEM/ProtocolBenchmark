import pika
import base64
import numpy as np
import imageio as iio
import matplotlib.pyplot as plt
from threading import Thread, Event

def message_callback(ch, method, properties, body):
    message = body.decode('utf-8')
    print(f" [x] Received message: {message}")

def video_callback(ch, method, properties, body, stop_event, writer, ax):
    if stop_event.is_set():
        ch.stop_consuming()
        return
    
    # Decode the base64 string back to bytes
    img_data = base64.b64decode(body)
    
    # Convert bytes data to numpy array and read the image
    img_np = iio.imread(img_data, format='jpg')

    # Write the frame to the video file
    writer.append_data(img_np)
    
    # Display the frame
    ax.clear()
    ax.imshow(img_np)
    plt.draw()
    plt.pause(0.001)

def consume_message():
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='hello')

    # Set up subscription on the queue
    channel.basic_consume(queue='hello',
                          on_message_callback=message_callback,
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def consume_video(stop_event):
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='video_queue')

    # Create VideoWriter object using imageio
    writer = iio.get_writer('received_video.mp4', fps=20)  # Adjust the frame rate as needed

    # Set up subscription on the queue
    fig, ax = plt.subplots()
    plt.ion()

    channel.basic_consume(queue='video_queue',
                          on_message_callback=lambda ch, method, properties, body: video_callback(ch, method, properties, body, stop_event, writer, ax),
                          auto_ack=True)

    print(' [*] Waiting for video stream. To exit press CTRL+C')
    channel.start_consuming()

    # Release the video writer
    writer.close()
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    # Start both consumers in separate threads
    Thread(target=consume_message).start()

    stop_event = Event()
    video_thread = Thread(target=consume_video, args=(stop_event,))
    video_thread.start()

    # Wait for user input to stop
    input("Press Enter to stop consuming video...\n")
    stop_event.set()
    video_thread.join()
