#!/usr/bin/env python3
import pika
import sys
import json
import random

if len(sys.argv) != 3:
   print("Usage: " + sys.argv[0] + " <queueName> <count>")
   sys.exit(1)

queue  = sys.argv[1]
count = int(sys.argv[2])

print("count:\t%d\nqueue:\t%s" % (count, queue) )

msgBody = {
        "device_name" :  "device",
	"temperature" : 0.0,
	"latitude" : 0.0,
	"longitude": 0.0
        }

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue = queue)

properties = pika.BasicProperties(content_type='application/json', delivery_mode=1, priority=1, content_encoding='utf-8')
for i in range(1, count):
    msgBody["device_name"] = "device " + str(i)	
    msgBody["temperature"] = round(random.uniform(-40, 56.7), 1)
    msgBody["latitude"] = random.uniform(-90, 90)
    msgBody["longitude"] = random.uniform(-180, 180)
    jsonStr = json.dumps(msgBody)
    properties.message_id = str(i)
    channel.basic_publish(exchange = '', routing_key = queue, body = jsonStr, properties = properties)
    print("Send\t%r" % msgBody)

connection.close()
print('Exiting')
