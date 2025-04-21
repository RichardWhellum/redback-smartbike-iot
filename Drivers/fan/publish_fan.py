#!/usr/bin/env python3
from mqtt_client import MQTTClient
import os
import sys
import json

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <level>")
        print("Where <level> is an integer from 0 to 5")
        exit(1)

    try:
        level = int(sys.argv[1])
        if level < 0 or level > 5:
            raise ValueError
    except ValueError:
        print("Level must be an integer between 0 and 5.")
        exit(1)

    try:
        mqtt_client = MQTTClient(
            os.getenv('MQTT_HOSTNAME'),
            os.getenv('MQTT_USERNAME'),
            os.getenv('MQTT_PASSWORD')
        )
        mqtt_client.setup_mqtt_client()
        device_id = os.getenv('DEVICE_ID')

        topic = f"bike/{device_id}/fan/control"
        payload = json.dumps({"level": level})

        print(f"Publishing to {topic} with payload: {payload}")
        mqtt_client.publish(topic, payload)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
