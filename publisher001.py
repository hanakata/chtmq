import paho.mqtt.client as mqtt
import sys
import datetime
import subprocess

username = input('input username:')

subscriber_run = 'C:\git\chtmq\subscriber001.py'
subprocess.run(subscriber_run, shell=True)

host = '127.0.0.1'
port = 1883
topic = '00001/local/' + username
_qos = 1
retain = 0
message = sys.argv

client = mqtt.Client(protocol=mqtt.MQTTv311)

client.connect(host, port=port, keepalive=60)

def on_connect(client, userdata, flags, respons_code):
    user = topic.split('/')
    print(user[0])

    client.subscribe(topic, qos = _qos)

def on_message(client, userdata, msg):
    d = datetime.datetime.today()
    reception_time = '%s:%s:%s' % (d.hour, d.minute, d.second)
    print(reception_time + ' ' + str(msg.payload))

def on_publish(msg):
    client.publish(topic, msg, _qos, retain)

if __name__ == '__main__':
    while True:
        message = input('>>>  ')
        on_publish(message)
