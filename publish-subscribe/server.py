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
    sock.bind(host)

    print "Hit Ctrl-C to stop broadcasting."
    print
    time.sleep(1.0)

    try:
        for n in itertools.count():            
            event = {"id": str(uuid.uuid1()), "count": n}
            js = json.dumps(event)
            print js
            sock.send(js)

            time.sleep(2)
    except KeyboardInterrupt:
        pass

    print "Waiting for message queues to flush..."
    time.sleep(0.5)
    print "Done."

if __name__ == "__main__":
    main()