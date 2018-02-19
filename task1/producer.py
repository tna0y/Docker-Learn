#!/usr/bin/env python3
import pika

rmq_conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = rmq_conn.channel()

channel.queue_declare(queue='task1')


print('Enter your message to store in MongoDB.')
while True:
    inp = input('> ')
    channel.basic_publish(exchange='',
                      routing_key='task1',
                                            body=inp)
    print("[x] Sent '%s'" % inp)
connection.close()
