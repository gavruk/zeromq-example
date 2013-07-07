#!/usr/bin/env python

import random
import time

import zmq

def main():
    host = "tcp://127.0.0.1:5554"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.PAIR)
    sock.bind(host)

    client_id = random.randint(0, 100)
    try:
        while True:
            sock.send("Hello from server")
            msg = sock.recv()
            print msg
            time.sleep(1)
    except:
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()