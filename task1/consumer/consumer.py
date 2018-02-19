#!/usr/bin/env python3

from pymongo import MongoClient
import pika

db = MongoClient('mongodb://mongodb:27017/')['promprog']


rmq_conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))

channel = rmq_conn.channel()

channel.queue_declare(queue='task1')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    db['messages'].insert({'message': body, 'queue': 'task1'})


channel.basic_consume(callback, queue='task1', no_ack=True)

channel.start_consuming()
