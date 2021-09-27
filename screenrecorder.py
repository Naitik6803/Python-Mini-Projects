import time
from tkinter import *
import os
import cv2
import numpy as np
from PIL import ImageGrab
import threading
import datetime
from win32api import GetSystemMetrics
import tkinter.messagebox


window = Tk()
window.geometry("500x200+460+170")
window.resizable(0, 0)
window.configure(bg='#030818')

recording = threading.Event()
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)



def recorder():

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fps = 20.0
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    output = cv2.VideoWriter(f"{time_stamp}.mp4", fourcc, fps, (width, height))
    recording.set()
    while recording.is_set():

        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        output.write(frame)
    output.release()
    cv2.destroyAllWindows()


def start_recording():
    if not recording.is_set():
        threading.Thread(target=recorder).start()
    button['text'] = 'Stop Recording'
    button['bg'] = 'red'
    button['fg'] = 'white'


def stop_recording():
    recording.clear()
    button['text'] = "Start Recording"
    button['bg'] = 'gray'
    button['fg'] = 'white'
    text = Label(text="Your recoding has been saved!")
    text.place(relx=0.5, rely=0.9, anchor=CENTER)
    window.after(2000, text.destroy)

def changeText():
    button['text'] = 'Submitted'



def toggleText():
    if (button['text'] == "Start Recording"):

        start_recording()

    else:


        stop_recording()


button=Button(window, text="Start Recording", command=toggleText, bd=0, bg="gray",fg="white",font=("Helvetica", 15, "bold"))
button.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()