#!/usr/bin/env python

import time
import uuid

import zmq


def main():
    host = "tcp://127.0.0.1:5554"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUSH)
    sock.bind(host)

    try:
        for num in xrange(2000):
            message = { 'id': str(uuid.uuid1()) }
            sock.send_json(message)
    except:
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()