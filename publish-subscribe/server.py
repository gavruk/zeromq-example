#!/usr/bin/env python

import itertools
import time
import uuid

import zmq

def main():
    host = "tcp://127.0.0.1:5554"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.bind(host)

    try:
        for n in itertools.count():            
            event = {"id": str(uuid.uuid1()), "count": n}
            print event
            sock.send_json(event)

            time.sleep(2)
    except:
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()