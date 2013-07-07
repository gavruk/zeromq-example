#!/usr/bin/env python

import sys
import time

import zmq

def main():
    host = "tcp://127.0.0.1:5555"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.SUB)
    sock.setsockopt(zmq.SUBSCRIBE, '')
    sock.connect(host)
    
    try:
        while True:
            event = sock.recv()
            print event
    except KeyboardInterrupt:
        pass
    print "Done."

if __name__ == "__main__":
    main()