#!/usr/bin/env python

import random

import zmq

def main():
    host = "tcp://127.0.0.1:5554"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.REQ)
    sock.connect(host)
    
    client_id = random.randint(0, 100)
    try:
        while True:            
            sock.send("Handling message from client %s" % client_id)
            event = sock.recv()
            print event
    except:
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()