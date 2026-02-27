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


## Installation

### 1. Clone or Download Project

Place the following files in one folder:

- publisher.py
- subscriber.py
- requirements.txt


### 2. Install Dependencies

pip install -r requirements.txt


### 3. Install MQTT Broker

Linux (Ubuntu):

sudo apt update
sudo apt install mosquitto mosquitto-clients

Start broker:

mosquitto

Windows:

Download Mosquitto from:
https://mosquitto.org/download/

Start the Mosquitto broker after installation.

Default Configuration:
Broker: localhost
Port: 1883
Topic: security/face_alert


## How to Run

### Step 1: Start MQTT Broker

mosquitto

### Step 2: Start Subscriber (Monitoring System)

python subscriber.py

### Step 3: Start Publisher (Camera System)

python publisher.py


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
