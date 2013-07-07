#!/usr/bin/env python

import itertools
import time
import json
import uuid

import zmq

def main():
    host = host = "tcp://127.0.0.1:5555"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.REP)
    sock.connect(host)

    try:
        for n in itertools.count():
            recieved_message = sock.recv()
            print recieved_message
            
            event = {"id": str(uuid.uuid1()), "count": n}
            js = json.dumps(event)
            print js
            sock.send(js)

            time.sleep(2)
    except:
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()