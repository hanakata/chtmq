from time import sleep
import paho.mqtt.client as mqtt
import sys
import datetime

host = '127.0.0.1'
port = 1883
topic = '00001/local/shara'
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
#    print(msg.topic + ' ' + str(msg.payload))
    d = datetime.datetime.today()
    reception_time = '%s:%s:%s' % (d.hour, d.minute, d.second)
    print(reception_time + ' ' + str(msg.payload))

def on_publish(msg):
    client.publish(topic, msg, _qos, retain)

if __name__ == '__main__':
    while True:
        message = input('>>>  ')
        on_publish(message)




        

#        client.loop_forever()