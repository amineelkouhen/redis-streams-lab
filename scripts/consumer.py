#!/usr/bin/env python3
import pika
import sys
import json
import redis

if len(sys.argv) != 2:
   print("Usage: " + sys.argv[0] + " <queueName>")
   sys.exit(1)

queue = sys.argv[1]

print("queue:\t%s" % (queue) )

pool = redis.ConnectionPool(host='redis-12000.cluster.redis-process.demo.redislabs.com', port=12000)
r = redis.Redis(connection_pool=pool)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue = queue)

def callback(ch, method, properties, body):
    msgBody = json.loads(body)
    r.xadd(queue, msgBody)
    print("Receive\t%r" % msgBody)

channel.basic_consume(queue = queue,
                      auto_ack=True,
                      on_message_callback=callback)

print('Waiting for messages. To exit press CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('Exiting')
