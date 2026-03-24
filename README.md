# 🤖 Gesture Controlled Robotic Arm using OpenCV & Raspberry Pi

---

## 📌 Overview
This project implements a real-time gesture-controlled robotic arm system using computer vision and embedded control.

A webcam captures hand gestures, which are processed using OpenCV and MediaPipe on a Raspberry Pi. Based on the number of fingers detected, control signals are generated to move servo motors of a robotic arm.

---

## 🎯 Objectives
- To implement real-time hand gesture recognition
- To control a robotic arm using vision-based input
- To integrate software (OpenCV) with hardware (Raspberry Pi & servos)

---

## ⚙️ System Working

1. Camera captures live video
2. OpenCV processes the video frames
3. MediaPipe detects hand landmarks
4. Finger counting algorithm determines gesture
5. Raspberry Pi generates PWM signals
6. Servo motors move according to detected gesture

---

## 🧠 System Architecture

Camera → OpenCV → MediaPipe → Finger Detection → Raspberry Pi → Servo Driver → Robotic Arm

---

## 🧩 Block Diagram

![Block Diagram](images/block_diagram.png)

---

## 💻 Software Requirements

- Python 3.10+
- OpenCV
- MediaPipe
- NumPy
- RPi.GPIO (for Raspberry Pi)

Install all dependencies:

```bash
pip install -r requirements.txt
🔌 Hardware Requirements
| Component    | Specification                       |
| ------------ | ----------------------------------- |
| Raspberry Pi | Raspberry Pi 4 / 5                  |
| Camera       | USB Webcam                          |
| Servo Motor  | SG90 / MG90S                        |
| Servo Driver | PCA9685 (recommended)               |
| Power Supply | 5V 2A (Pi) + 5V External for servos |
| Jumper Wires | Male-Female                         |
🔧 Hardware Connections
| PCA9685 | Raspberry Pi |
| ------- | ------------ |
| VCC     | 5V           |
| GND     | GND          |
| SDA     | GPIO2        |
| SCL     | GPIO3        |
⚠️ Important:
Do NOT power servos directly from Raspberry Pi
📂 Project Structure
gesture_detection/
   └── hand_tracking.py

servo_control/
   └── servo_driver.py

requirements.txt
README.md
images/
▶️ How to Run
Step 1: Install Dependencies
pip install -r requirements.txt
Step 2: Run Gesture Detection
python gesture_detection/hand_tracking.py
Step 3: Run Servo Control (on Raspberry Pi)
python servo_control/servo_driver.py
🎮 Gesture Mapping
Fingers Detected	Action
0	Servo → 0°
1	Servo → 45°
2	Servo → 90°
3	Servo → 120°
4	Servo → 150°
5	Servo → 180°
⚠️ Challenges Faced
Servo jitter due to unstable power
MediaPipe compatibility with Python versions
Real-time processing delay
🔮 Future Scope
Multi-servo robotic arm (5 DOF)
Wireless control using WiFi/Bluetooth
AI-based gesture classification (ML model)
Mobile app integration
👨‍💻 Author

Gauri
Instrumentation & Control Engineering
VIT Pune

⭐ Acknowledgment
OpenCV Documentation
MediaPipe by Google
Raspberry Pi Community

