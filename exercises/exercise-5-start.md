<img src="../img/redis-logo-full-color-rgb.png" height=100/>

# Demo 1 - From RabbitMQ to Redis Streams

We're finally going to look at how we can programmatically work with Redis. In this case we'll use Python leveraging the [redis-py client](https://github.com/redis/redis-py) to interact with Redis core data structures, and especially Streams.

Let's get started!

## Install and deploy RabbitMQ broker
From a terminal session, install the RabbitMQ broker. For a macOS environment, you can use homebrew :

```shell
brew update
brew install rabbitmq
```

Configure the terminal environment to include the RabbitMQ sbin folder in the PATH:

```shell
export PATH=$PATH:/usr/local/opt/rabbitmq/sbin
```
In a new terminal session, start the RabbitMQ broker:

```
rabbitmq-server
```

Do a health check using the rabbitmqctl status command:

```
rabbitmqctl status
``` 

## Goals

After this exercise you will have a running app that consumes RabbitMQ messages and put store them as streams in Redis. The first piece of code consists of a RabbitMQ producer. The producer simulates sensors that send geographical coordinates and temperatures from different locations.

```python
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
```

To execute this code successfully, you need Python3 installed as well as json and pika packages.
```
pip3 install pika
pip3 install json
```

* Run the [producer](../scripts/producer.py) script with the following arguments:
```
./producer.py [QUEUE_NAME] [ITERATION]
```

In the other side, you need another script that consumes the RabbitMQ queue and creates entries in a Redis stream with having the same name as the queue. For this, you need to execute the following code :

```python
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

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
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
```
This piece of code is self-explainatory. It starts consuming the channel (queue name is given as an argument) then, run a callback function for each message consumed in the queue. In the callback function, the XADD command is executed to create an entry in Redis with the RabbitMQ message payload.

* Run the [consumer](../scripts/consumer.py) script with the following arguments:
```
./consumer.py [QUEUE_NAME]
```

## Next steps

Great! We created our first app interacting with Redis through the python client (redis-py). In the next [exercise](exercise-6-start.md), we will try to ingest plain files into Redis streams. 
