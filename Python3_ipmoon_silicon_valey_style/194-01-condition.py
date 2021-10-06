import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1(condition: threading.Condition):
    with condition:
        condition.wait()
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")


def worker2(condition: threading.Condition):
    with condition:
        condition.wait()
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")


def worker3(condition: threading.Condition):
    with condition:
        logging.debug("start")
        time.sleep(5)
        logging.debug("end")
        condition.notifyAll()


if __name__ == "__main__":
    condition = threading.Condition()

    ts = []
    t1 = threading.Thread(target=worker1, args=(condition,))
    t2 = threading.Thread(target=worker2, args=(condition,))
    t3 = threading.Thread(target=worker3, args=(condition,))
    ts.extend((t1, t2, t3))
    [t.start() for t in ts]
    [t.join() for t in ts]