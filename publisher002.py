from time import sleep
import paho.mqtt.client as mqtt

host = '127.0.0.1'
port = 1883
topic = '0801920/a'

client = mqtt.Client(protocol=mqtt.MQTTv311)

client.connect(host, port=port, keepalive=60)

for i in range(3):
    client.publish(topic, 'tel')
    sleep(0.2)

client.disconnect()