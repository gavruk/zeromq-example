#!/usr/bin/env python

import pprint
import itertools

import zmq


def main():
    host = "tcp://127.0.0.1:5555"

    ctx = zmq.Context()
    sock = ctx.socket(zmq.PULL)
    sock.bind(host)

    try:
        collected_data = {}
        while True:
            for _ in itertools.repeat(None, 1000):
                message = sock.recv_json()
                from_consumer = message['consumer'];
                if collected_data.has_key(from_consumer):
                    collected_data[from_consumer] = collected_data[from_consumer] + 1
                else:
                    collected_data[from_consumer] = 1
            pprint.pprint(collected_data)
    except Exception, e:
        print e
        pass
    finally:
        sock.close()
        ctx.term()

if __name__ == "__main__":
    main()