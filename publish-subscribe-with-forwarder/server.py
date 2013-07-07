#!/usr/bin/env python

import itertools
import time
import json
import uuid

import zmq

def main():
    host = "tcp://127.0.0.1:5554"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.connect(host)

    try:
        for n in itertools.count():            
            event = {"id": str(uuid.uuid1()), "count": n}
            js = json.dumps(event)
            print js
            sock.send(js)

            time.sleep(1)
    except:
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()