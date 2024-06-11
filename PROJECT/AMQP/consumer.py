# # # # import pika
# # # # import base64
# # # # import cv2
# # # # import numpy as np

# # # # def message_callback(ch, method, properties, body):
# # # #     message = body.decode('utf-8')
# # # #     print(f" [x] Received message: {message}")

# # # # def image_callback(ch, method, properties, body):
# # # #     print(" [x] Received image")
    
# # # #     # Decode the base64 string back to bytes
# # # #     img_data = base64.b64decode(body)
    
# # # #     # Convert bytes data to numpy array
# # # #     nparr = np.frombuffer(img_data, np.uint8)
    
# # # #     # Decode numpy array to image
# # # #     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
# # # #     # Save the received image to disk
# # # #     cv2.imwrite('received_image.jpg', img)
# # # #     print(" [x] Image saved as 'received_image.jpg'")

# # # #     # Display the image
# # # #     cv2.imshow('Received Image', img)
# # # #     cv2.waitKey(0)
# # # #     cv2.destroyAllWindows()

# # # # def consume_message():
# # # #     # Connect to RabbitMQ server
# # # #     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# # # #     channel = connection.channel()

# # # #     # Declare a queue
# # # #     channel.queue_declare(queue='hello')

# # # #     # Set up subscription on the queue
# # # #     channel.basic_consume(queue='hello',
# # # #                           on_message_callback=message_callback,
# # # #                           auto_ack=True)

# # # #     print(' [*] Waiting for messages. To exit press CTRL+C')
# # # #     channel.start_consuming()

# # # # def consume_image():
# # # #     # Connect to RabbitMQ server
# # # #     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# # # #     channel = connection.channel()

# # # #     # Declare a queue
# # # #     channel.queue_declare(queue='image_queue')

# # # #     # Set up subscription on the queue
# # # #     channel.basic_consume(queue='image_queue',
# # # #                           on_message_callback=image_callback,
# # # #                           auto_ack=True)

# # # #     print(' [*] Waiting for images. To exit press CTRL+C')
# # # #     channel.start_consuming()

# # # # if __name__ == "__main__":
# # # #     from threading import Thread

# # # #     # Start both consumers in separate threads
# # # #     Thread(target=consume_message).start()
# # # #     Thread(target=consume_image).start()

# # # import pika
# # # import base64
# # # import cv2
# # # import numpy as np

# # # def message_callback(ch, method, properties, body):
# # #     message = body.decode('utf-8')
# # #     print(f" [x] Received message: {message}")

# # # def image_callback(ch, method, properties, body):
# # #     print(" [x] Received image")
    
# # #     # Decode the base64 string back to bytes
# # #     img_data = base64.b64decode(body)
    
# # #     # Convert bytes data to numpy array
# # #     nparr = np.frombuffer(img_data, np.uint8)
    
# # #     # Decode numpy array to image
# # #     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
# # #     # Save the received image to disk
# # #     cv2.imwrite('received_image.jpg', img)
# # #     print(" [x] Image saved as 'received_image.jpg'")

# # #     # Display the image
# # #     cv2.imshow('Received Image', img)
# # #     cv2.waitKey(0)
# # #     cv2.destroyAllWindows()

# # # def consume_message():
# # #     # Connect to RabbitMQ server
# # #     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# # #     channel = connection.channel()

# # #     # Declare a queue
# # #     channel.queue_declare(queue='hello')

# # #     # Set up subscription on the queue
# # #     channel.basic_consume(queue='hello',
# # #                           on_message_callback=message_callback,
# # #                           auto_ack=True)

# # #     print(' [*] Waiting for messages. To exit press CTRL+C')
# # #     channel.start_consuming()

# # # def consume_image():
# # #     # Connect to RabbitMQ server
# # #     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# # #     channel = connection.channel()

# # #     # Declare a queue
# # #     channel.queue_declare(queue='image_queue')

# # #     # Set up subscription on the queue
# # #     channel.basic_consume(queue='image_queue',
# # #                           on_message_callback=image_callback,
# # #                           auto_ack=True)

# # #     print(' [*] Waiting for images. To exit press CTRL+C')
# # #     channel.start_consuming()

# # # if __name__ == "__main__":
# # #     from threading import Thread

# # #     # Start both consumers in separate threads
# # #     Thread(target=consume_message).start()
# # #     Thread(target=consume_image).start()

# # import pika
# # import base64
# # import cv2
# # import numpy as np

# # def message_callback(ch, method, properties, body):
# #     message = body.decode('utf-8')
# #     print(f" [x] Received message: {message}")

# # def video_callback(ch, method, properties, body):
# #     # Decode the base64 string back to bytes
# #     img_data = base64.b64decode(body)
    
# #     # Convert bytes data to numpy array
# #     nparr = np.frombuffer(img_data, np.uint8)
    
# #     # Decode numpy array to image
# #     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
# #     # Display the frame
# #     cv2.imshow('Received Video', img)
# #     cv2.waitKey(1)

# # def consume_message():
# #     # Connect to RabbitMQ server
# #     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# #     channel = connection.channel()

# #     # Declare a queue
# #     channel.queue_declare(queue='hello')

# #     # Set up subscription on the queue
# #     channel.basic_consume(queue='hello',
# #                           on_message_callback=message_callback,
# #                           auto_ack=True)

# #     print(' [*] Waiting for messages. To exit press CTRL+C')
# #     channel.start_consuming()

# # def consume_video():
# #     # Connect to RabbitMQ server
# #     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# #     channel = connection.channel()

# #     # Declare a queue
# #     channel.queue_declare(queue='video_queue')

# #     # Set up subscription on the queue
# #     channel.basic_consume(queue='video_queue',
# #                           on_message_callback=video_callback,
# #                           auto_ack=True)

# #     print(' [*] Waiting for video stream. To exit press CTRL+C')
# #     channel.start_consuming()

# # if __name__ == "__main__":
# #     from threading import Thread

# #     # Start both consumers in separate threads
# #     Thread(target=consume_message).start()
# #     Thread(target=consume_video).start()

# #     # To close the video window gracefully
# #     try:
# #         while True:
# #             pass
# #     except KeyboardInterrupt:
# #         cv2.destroyAllWindows()

# import pika
# import base64
# import cv2
# import numpy as np
# from threading import Thread

# def message_callback(ch, method, properties, body):
#     message = body.decode('utf-8')
#     print(f" [x] Received message: {message}")

# def video_callback(ch, method, properties, body):
#     # Decode the base64 string back to bytes
#     img_data = base64.b64decode(body)
    
#     # Convert bytes data to numpy array
#     nparr = np.frombuffer(img_data, np.uint8)
    
#     # Decode numpy array to image
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
#     # Display the frame
#     cv2.imshow('Received Video', img)
#     cv2.waitKey(1)

# def consume_message():
#     # Connect to RabbitMQ server
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()

#     # Declare a queue
#     channel.queue_declare(queue='hello')

#     # Set up subscription on the queue
#     channel.basic_consume(queue='hello',
#                           on_message_callback=message_callback,
#                           auto_ack=True)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()

# def consume_video():
#     # Connect to RabbitMQ server
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()

#     # Declare a queue
#     channel.queue_declare(queue='video_queue')

#     # Set up subscription on the queue
#     channel.basic_consume(queue='video_queue',
#                           on_message_callback=video_callback,
#                           auto_ack=True)

#     print(' [*] Waiting for video stream. To exit press CTRL+C')
#     channel.start_consuming()

# if __name__ == "__main__":
#     # Start both consumers in separate threads
#     Thread(target=consume_message).start()
#     video_thread = Thread(target=consume_video)
#     video_thread.start()

#     # Wait for user input to stop
#     input("Press Enter to stop consuming video...\n")
#     video_thread.join()

#     # To close the video window gracefully
#     cv2.destroyAllWindows()

# import pika
# import base64
# import cv2
# import numpy as np
# from threading import Thread, Event

# def message_callback(ch, method, properties, body):
#     message = body.decode('utf-8')
#     print(f" [x] Received message: {message}")

# def video_callback(ch, method, properties, body, stop_event):
#     if stop_event.is_set():
#         ch.stop_consuming()
#         return
    
#     # Decode the base64 string back to bytes
#     img_data = base64.b64decode(body)
    
#     # Convert bytes data to numpy array
#     nparr = np.frombuffer(img_data, np.uint8)
    
#     # Decode numpy array to image
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
#     # Display the frame
#     cv2.imshow('Received Video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         stop_event.set()
#         ch.stop_consuming()

# def consume_message():
#     # Connect to RabbitMQ server
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()

#     # Declare a queue
#     channel.queue_declare(queue='hello')

#     # Set up subscription on the queue
#     channel.basic_consume(queue='hello',
#                           on_message_callback=message_callback,
#                           auto_ack=True)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()

# def consume_video(stop_event):
#     # Connect to RabbitMQ server
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()

#     # Declare a queue
#     channel.queue_declare(queue='video_queue')

#     # Set up subscription on the queue
#     channel.basic_consume(queue='video_queue',
#                           on_message_callback=lambda ch, method, properties, body: video_callback(ch, method, properties, body, stop_event),
#                           auto_ack=True)

#     print(' [*] Waiting for video stream. To exit press CTRL+C')
#     channel.start_consuming()

# if __name__ == "__main__":
#     # Start both consumers in separate threads
#     Thread(target=consume_message).start()

#     stop_event = Event()
#     video_thread = Thread(target=consume_video, args=(stop_event,))
#     video_thread.start()

#     # Wait for user input to stop
#     input("Press Enter to stop consuming video...\n")
#     stop_event.set()
#     video_thread.join()

#     # To close the video window gracefully
#     cv2.destroyAllWindows()

import pika
import base64
import cv2
import numpy as np
from threading import Thread, Event

def message_callback(ch, method, properties, body):
    message = body.decode('utf-8')
    print(f" [x] Received message: {message}")

def video_callback(ch, method, properties, body, stop_event, out):
    if stop_event.is_set():
        ch.stop_consuming()
        return
    
    # Decode the base64 string back to bytes
    img_data = base64.b64decode(body)
    
    # Convert bytes data to numpy array
    nparr = np.frombuffer(img_data, np.uint8)
    
    # Decode numpy array to image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Write the frame to the video file
    out.write(img)
    
    # Display the frame
    cv2.imshow('Received Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop_event.set()
        ch.stop_consuming()

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

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('received_video.avi', fourcc, 20.0, (640, 480))  # Adjust the frame size accordingly

    # Set up subscription on the queue
    channel.basic_consume(queue='video_queue',
                          on_message_callback=lambda ch, method, properties, body: video_callback(ch, method, properties, body, stop_event, out),
                          auto_ack=True)

    print(' [*] Waiting for video stream. To exit press CTRL+C')
    channel.start_consuming()

    # Release the video writer
    out.release()

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

    # To close the video window gracefully
    cv2.destroyAllWindows()
