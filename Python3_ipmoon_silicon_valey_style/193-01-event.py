import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1(event):
    event.wait()
    logging.debug("start")
    logging.debug("end")


def worker2(event):
    event.wait()
    logging.debug("start")
    logging.debug("end")


def worker3(event):
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")
    event.set()


if __name__ == "__main__":
    event = threading.Event()

    ts = []
    t1 = threading.Thread(target=worker1, args=(event,))
    t2 = threading.Thread(target=worker2, args=(event,))
    t3 = threading.Thread(target=worker3, args=(event,))
    ts.extend((t1, t2, t3))
    [t.start() for t in ts]
    [t.join() for t in ts]