#!/usr/bin/env python

import uuid

import zmq


def main():
    host = "tcp://127.0.0.1:5554"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUSH)
    sock.connect(host)

    try:
        for num in xrange(100):
            message = { 'id': str(uuid.uuid1()), 'num': num }
            sock.send_json(message)
    except:
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()