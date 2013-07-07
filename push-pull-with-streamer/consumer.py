#!/usr/bin/env python

import zmq
import random

def main():
    host = "tcp://127.0.0.1:5555"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.PULL)
    sock.connect(host)
    
    consumer_id = "client #%s" % random.randint(0, 100)
    print consumer_id

    try:
        while True:
            data = sock.recv_json()
            num = data['num']
            result = { 'consumer' : consumer_id, 'num' : num}
            print result
    except:
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()