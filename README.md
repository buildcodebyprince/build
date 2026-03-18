# 🚧 Smart Road Safety Detection System

## 📌 Overview
The **Smart Road Safety Detection System** is a computer vision–based project that detects **potholes and speed breakers** in real time using a webcam. It improves road safety by estimating the distance to hazards and suggesting a safe driving speed.

---

## 🎯 Features
- 📷 Real-time video processing using OpenCV  
- 🛣️ Detects potholes and speed breakers  
- 📏 Calculates distance from hazard  
- 🚗 Suggests safe driving speed  
- 🔴🟢 Traffic signal indicator (STOP / GO)  
- 🔊 Sound alert for nearby hazards  
- 🖥️ GUI built with Tkinter  

---

## 🛠️ Technologies Used
- Python  
- OpenCV  
- NumPy  
- Tkinter  
- PIL (Pillow)  
- Winsound  

---

## ⚙️ How It Works
1. Captures live video from webcam  
2. Converts frame to grayscale  
3. Applies Gaussian blur to reduce noise  
4. Detects edges using Canny Edge Detection  
5. Finds contours (potential hazards)  
6. Filters contours based on size  
7. Calculates distance using formula:

   Distance = (Real Width × Focal Length) / Object Width  

8. Displays:
   - Distance from hazard  
   - Suggested speed  
   - Road status  

---

## 📊 System Output
- **Road Clear** → Green signal, normal speed  
- **Hazard Detected** → Red signal, reduced speed + beep alert  

---

## 🧪 Parameters Used
- REAL_WIDTH = 0.5 meters  
- FOCAL_LENGTH = 700  

---

## ▶️ How to Run

### 1. Install Dependencies
```bash
pip install opencv-python numpy pillow
2. Run the Program
python main.py
🖼️ GUI Components

Live camera feed

Distance display

Speed suggestion

Status indicator

Traffic light system

⚠️ Limitations

Works best in good lighting conditions

Accuracy depends on camera quality

Not fully reliable for all road types

🚀 Future Improvements

AI/Deep Learning integration

GPS-based alerts

Mobile app support

Night detection improvements


