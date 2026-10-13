import paho.mqtt.client as mqtt

BROKER = "192.168.1.60"
TOPIC = "lab/test"
MESSAGE = "hello from Python"
PORT = 1883

client = mqtt.Client()

try:
    client.connect(BROKER, 1883, 60)
    client.publish(TOPIC, MESSAGE)
    print(f"Published '{MESSAGE}' to '{TOPIC}'")
    client.disconnect()
except Exception as e:
    print(f"Error: {e}")