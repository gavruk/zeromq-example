#!/usr/bin/env python

import zmq

def main():
    frontend_host = "tcp://127.0.0.1:5554"
    backend_host = "tcp://127.0.0.1:5555"    

    try:
        ctx = zmq.Context(1)
        
        frontend = ctx.socket(zmq.SUB)
        frontend.bind(frontend_host)
        frontend.setsockopt(zmq.SUBSCRIBE, '')

        backend = ctx.socket(zmq.PUB)
        backend.bind(backend_host)

        zmq.device(zmq.FORWARDER, frontend, backend)
    except KeyboardInterrupt, Exception:
        print "bringing down zmq device"
    finally:
        pass
        frontend.close()
        backend.close()
        ctx.term()

if __name__ == "__main__":
    main()