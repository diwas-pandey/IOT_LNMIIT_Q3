# IOT_LNMIIT_Q3
# Real-Time Face Detection Alert System (OpenCV + MQTT)

## Overview

This project implements a real-time security monitoring system that:

- Captures live video from a camera
- Performs real-time human face detection using OpenCV
- Publishes alert messages via MQTT when a face is detected
- Subscribes to the alert topic and displays alerts in real time

The system consists of two programs:

1. publisher.py  → Camera + Face Detection + MQTT Publisher
2. subscriber.py → MQTT Subscriber (Monitoring System)

---

## System Architecture

Camera (OpenCV)  →  MQTT Broker  →  Monitoring System (Subscriber)

Topic Used:
security/face_alert

## Requirements

- Python 3.8+
- Webcam
- MQTT Broker (Mosquitto recommended)


## How It Works

1. OpenCV captures live video from the webcam.
2. Haar Cascade classifier detects faces in real time.
3. When a face is detected:
   - A JSON alert message is created.
   - The alert is published to topic: security/face_alert
4. The subscriber receives and displays the alert instantly

## Alert Message Format

{
  "event": "FACE_DETECTED",
  "timestamp": "YYYY-MM-DD HH:MM:SS",
  "faces_count": number_of_faces,
  "location": "Restricted Area 1"
}

## Features
- Real-time face detection
- MQTT-based alert system
- Efficient event throttling (prevents message flooding)
- Lightweight JSON messaging
- Near real-time performance

## Author

Real-Time Object Detection Alert System using OpenCV and MQTT
