import paho.mqtt.client as mqtt
import json

BROKER = "localhost"
PORT = 1883
TOPIC = "security/face_alert"

def on_connect(client, userdata, flags, rc):
    print("Connected to broker.")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    alert = json.loads(msg.payload.decode())
    
    print("\n========== 🚨 SECURITY ALERT ==========")
    print("Event:", alert["event"])
    print("Time:", alert["timestamp"])
    print("Faces Detected:", alert["faces_count"])
    print("Location:", alert["location"])
    print("=======================================\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

print("Monitoring system started...")
client.loop_forever()