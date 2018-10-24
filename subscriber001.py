import paho.mqtt.client as mqtt
import datetime

host = '127.0.0.1'
port = 1883
topic = '00001/local/#'
_qos = 1

def on_connect(client, userdata, flags, respons_code):
    client.subscribe(topic, qos = _qos)

def on_message(client, userdata, msg):
    user = msg.topic.split('/')
    d = datetime.datetime.today()
    reception_time = '%s:%s:%s' % (d.hour, d.minute, d.second)
    print(reception_time + ' ' + user[2] + " " + str(msg.payload.decode('utf-8')))

if __name__ == '__main__':

    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port=port, keepalive=60)

    client.loop_forever()