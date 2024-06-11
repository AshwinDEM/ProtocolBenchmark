import tkinter as tk
from PIL import Image, ImageTk
import paho.mqtt.client as mqtt
import base64
import cv2
import numpy as np

class VideoCallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Call - Subscriber")
        
        self.video_label = tk.Label(self.root)
        self.video_label.pack()
        
        self.broker = 'localhost'  
        self.port = 1883
        self.topic = 'video'
        
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker, self.port, 60)
        
        self.client.loop_start()
        
    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        client.subscribe(self.topic)
        
    def on_message(self, client, userdata, msg):
        decoded_frame = base64.b64decode(msg.payload)
        np_arr = np.frombuffer(decoded_frame, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        
        self.video_label.imgtk = imgtk
        self.video_label.configure(image=imgtk)

def main():
    root = tk.Tk()
    app = VideoCallApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

