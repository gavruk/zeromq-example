#!/usr/bin/env python

import time

import zmq

def main():
    host = "tcp://127.0.0.1:5554"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.SUB)
    sock.setsockopt(zmq.SUBSCRIBE, '')
    sock.bind(host)
    
    try:
        while True:
            event = sock.recv_json()
            print event
    except:
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()