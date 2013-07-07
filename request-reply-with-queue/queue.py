#!/usr/bin/env python

import zmq

def main():
    
    frontend_host = "tcp://127.0.0.1:5554"
    backend_host = "tcp://127.0.0.1:5555"

    try:
        ctx = zmq.Context(1)
        
        frontend = ctx.socket(zmq.ROUTER)
        frontend.bind(frontend_host)

        backend = ctx.socket(zmq.DEALER)
        backend.bind(backend_host)

        zmq.device(zmq.QUEUE, frontend, backend)
    except:
        pass
    finally:
        frontend.close()
        backend.close()
        ctx.term()

if __name__ == "__main__":
    main()