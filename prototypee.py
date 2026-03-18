import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
import winsound

# ---------------- PARAMETERS ----------------
REAL_WIDTH = 0.5
FOCAL_LENGTH = 700

# ---------------- GUI WINDOW ----------------
window = tk.Tk()
window.title("Smart Road Safety Detection System")
window.geometry("1100x720")
window.configure(bg="#0f172a")

title = tk.Label(window,
                 text="SMART ROAD SAFETY DETECTION SYSTEM",
                 font=("Arial",24,"bold"),
                 fg="#38bdf8",
                 bg="#0f172a")
title.pack(pady=10)

# ------------- VIDEO FRAME ----------------
video_frame = tk.Frame(window,bg="#0f172a")
video_frame.pack()

video_label = tk.Label(video_frame)
video_label.pack()

# ------------- INFORMATION PANEL -------------
info_frame = tk.Frame(window,bg="#0f172a")
info_frame.pack(pady=10)

distance_label = tk.Label(info_frame,
                          text="Distance : -- m",
                          font=("Arial",18,"bold"),
                          fg="#22d3ee",
                          bg="#0f172a")
distance_label.grid(row=0,column=0,padx=30)

speed_label = tk.Label(info_frame,
                       text="Suggested Speed : -- km/h",
                       font=("Arial",18,"bold"),
                       fg="#facc15",
                       bg="#0f172a")
speed_label.grid(row=0,column=1,padx=30)

status_label = tk.Label(window,
                        text="STATUS : ROAD CLEAR",
                        font=("Arial",18,"bold"),
                        fg="#4ade80",
                        bg="#0f172a")
status_label.pack(pady=10)

# ----------- TRAFFIC LIGHT PANEL -----------
signal_frame = tk.Frame(window,bg="#0f172a")
signal_frame.pack(pady=15)

canvas = tk.Canvas(signal_frame,width=160,height=70,bg="#0f172a",highlightthickness=0)
canvas.pack()

red_light = canvas.create_oval(10,10,60,60,fill="#374151")
green_light = canvas.create_oval(90,10,140,60,fill="#22c55e")

label_red = tk.Label(signal_frame,text="STOP",fg="red",bg="#0f172a",font=("Arial",12))
label_red.pack(side="left",padx=20)

label_green = tk.Label(signal_frame,text="GO",fg="green",bg="#0f172a",font=("Arial",12))
label_green.pack(side="right",padx=20)

# -------- CAMERA START --------
cap = cv2.VideoCapture(0)

def update_frame():

    ret, frame = cap.read()

    if ret:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        edges = cv2.Canny(blur,50,150)

        contours,_ = cv2.findContours(edges,
                                      cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)

        hazard_detected = False

        for cnt in contours:

            area = cv2.contourArea(cnt)

            if area > 1500:

                x,y,w,h = cv2.boundingRect(cnt)

                if w > 40 and h > 15:

                    distance = (REAL_WIDTH * FOCAL_LENGTH)/w

                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

                    distance_label.config(text=f"Distance : {distance:.2f} m")

                    if distance <= 15:

                        hazard_detected = True

                        status_label.config(
                            text="STATUS : SPEED BREAKER / POTHOLE AHEAD",
                            fg="#ef4444"
                        )

                        speed_label.config(
                            text="Suggested Speed : 20 km/h"
                        )

                        canvas.itemconfig(red_light, fill="#ef4444")
                        canvas.itemconfig(green_light, fill="#374151")

                        winsound.Beep(1500,200)

                    else:

                        speed_label.config(
                            text="Suggested Speed : 40 km/h"
                        )

        if not hazard_detected:

            status_label.config(
                text="STATUS : ROAD CLEAR",
                fg="#22c55e"
            )

            canvas.itemconfig(red_light, fill="#374151")
            canvas.itemconfig(green_light, fill="#22c55e")

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

    video_label.after(10,update_frame)

update_frame()

window.mainloop()

cap.release()