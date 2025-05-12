#!/usr/bin/env python3
from mqtt_client import MQTTClient
import os
import json

def message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode("utf-8"))
        print(f"[STATUS] Topic: {msg.topic} → Level: {payload['value']}%")
    except Exception as e:
        print(f"[ERROR] Failed to parse message: {e}")

mqtt_client = MQTTClient(
    os.getenv('MQTT_HOSTNAME'),
    os.getenv('MQTT_USERNAME'),
    os.getenv('MQTT_PASSWORD')
)
mqtt_client.setup_mqtt_client()
device_id = os.getenv('DEVICE_ID')

mqtt_client.subscribe(f"bike/{device_id}/fan/status")
mqtt_client.get_client().on_message = message
mqtt_client.loop_forever()
