#!/usr/bin/env python

import time

import zmq

def main():
    host = "tcp://127.0.0.1:5554"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.PAIR)
    sock.connect(host)

    try:
        sock.send("hello")
        while True:
            msg = sock.recv()
            print msg
            sock.send("Hello from client")
            time.sleep(1)
    except:
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()