import logging
import queue
import threading

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1(queue):
    logging.debug("start")
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()
    logging.debug("longggggggggggggggggggggg")
    logging.debug("end")


if __name__ == "__main__":
    queue = queue.Queue()
    # 자료 갯수를 충분히 늘린다.
    for i in range(1000):
        queue.put(i)
    # 쓰레드를 여러개 생성하여 리스트에 담는다
    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker1, args=(queue,))
        t.start()
        ts.append(t)
    logging.debug("tasks are not done")
    # queue 는 하나만 생성했으니 join() 한번만 해도 된다
    queue.join()
    logging.debug("tasks are done")
    # queue 에서 None 을 빼가는(get) 것은 각 쓰레드이다.
    # 한 쓰레드가 가져가면 다른 쓰레드에겐 None 을 찾을 수 없으므로 blocking 상태가 된다.
    # 정상 동작하려면 쓰레드 갯수만큼 None 을 queue 에 넣어줘야 한다.
    queue.put(None)
    # 쓰레드 갯수만큼 각 쓰레드가 종료되기를 기다려준다. 만약 join() 안하면 현재 이 main 쓰레드가 자식 쓰레드보다 먼저 종료되면 자식 쓰레드는 모두 좀비 쓰레드가 된다.
    [t.join() for t in ts]