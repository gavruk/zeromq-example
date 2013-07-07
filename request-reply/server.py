#!/usr/bin/env python

import itertools
import time
import uuid

import zmq

def main():
    host = host = "tcp://127.0.0.1:5554"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.REP)
    sock.bind(host)

    try:
        for n in itertools.count():
            recieved_message = sock.recv()
            print recieved_message
            
            event = {"id": str(uuid.uuid1()), "count": n}
            print event
            sock.send_json(event)

            time.sleep(1)
    except:
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()