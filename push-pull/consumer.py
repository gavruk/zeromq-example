#!/usr/bin/env python

import time
import random

import zmq


def main():
    host_receiver = "tcp://127.0.0.1:5554"
    host_sender = "tcp://127.0.0.1:5555"

    ctx = zmq.Context()
    
    consumer_receiver = ctx.socket(zmq.PULL)
    consumer_receiver.connect(host_receiver)

    consumer_sender = ctx.socket(zmq.PUSH)
    consumer_sender.connect(host_sender)

    consumer_id = "client #%s" % random.randint(0, 100)
    print consumer_id

    try:
        while True:
            work = consumer_receiver.recv_json()
            result = { 'consumer' : consumer_id }
            consumer_sender.send_json(result)
    except:
        pass
    finally:
        consumer_receiver.close()
        consumer_sender.close()
        ctx.term()

if __name__ == "__main__":
    main()