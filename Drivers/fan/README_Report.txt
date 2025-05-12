
SmartBike VR – Fan Driver Rewrite Summary (Capstone Task)

Author: Lavesh Garg
Team: Redback Operations – IoT Subteam
Component: Wahoo HEADWIND Fan Driver

========================================
TASK OBJECTIVE:
- Fix the broken fan driver implementation
- Implement proper BLE GATT flow control
- Move away from speed-mapping logic to application control
- Use the correct MQTT topic: bike/{DEVICE_ID}/fan/control
- Publish fan status to: bike/{DEVICE_ID}/fan/status

========================================
WHAT WAS DONE:

1. fan.py (updated)
- Retained original gatt.DeviceManager structure
- Implemented BLE write flow using response-confirmed write_value()
- Subscribed to new MQTT topic 'fan/control'
- Accepted JSON payloads with "level" 0–5, mapped to 0–100% speed
- Published actual fan state to 'fan/status' topic
- Reused enable/start/send characteristic write cycles

2. publish_fan.py (updated)
- Sends JSON payloads like: {"level": 3}
- Writes to bike/{DEVICE_ID}/fan/control topic

3. subscriber.py (updated)
- Subscribes to bike/{DEVICE_ID}/fan/status
- Prints real-time fan speed values

4. mqtt_client.py (unchanged)
- Verified that the existing MQTTClient class handles secure connect/publish/subscribe as needed

========================================
CONFIG NOTES:
Environment variables used:
- DEVICE_ID
- MQTT_HOSTNAME
- MQTT_USERNAME
- MQTT_PASSWORD
- FAN_ADAPTER_NAME
- FAN_ALIAS_PREFIX

========================================
TESTING:
- Publish via CLI: `python3 publish_fan.py 3`
- View status output: `python3 subscriber.py`
- Run `fan.py` and confirm BLE connects to HEADWIND

All components are now modular, clean, and fully integrated.

