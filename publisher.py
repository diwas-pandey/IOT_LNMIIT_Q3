import cv2
import paho.mqtt.client as mqtt
import time
import json

BROKER = "localhost"
PORT = 1883
TOPIC = "security/face_alert"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

last_alert_time = 0
alert_interval = 5

print("System started. Monitoring restricted area...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    if len(faces) > 0:
        current_time = time.time()
        if current_time - last_alert_time > alert_interval:
            alert_message = {
                "event": "FACE_DETECTED",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "faces_count": len(faces),
                "location": "Restricted Area 1"
            }

            client.publish(TOPIC, json.dumps(alert_message))
            print("Alert Published:", alert_message)

            last_alert_time = current_time

    cv2.imshow("Security Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
client.disconnect()