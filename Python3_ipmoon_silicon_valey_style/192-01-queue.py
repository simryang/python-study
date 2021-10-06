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
    # queue.Queue 만 써도 이에 대한 락 처리 등이 자동으로 된다
    queue = queue.Queue()
    # 큐에 더미데이터 생성
    for i in range(10):
        queue.put(i)
    # worker1 함수를 쓰레드로 실행하고 인수로 여기에서 생성한 queue를 전달
    t1 = threading.Thread(target=worker1, args=(queue,))
    t1.start()
    logging.debug("tasks are not done")
    # 큐가 비워지지 않으면 queue join 이 완료되지 않음. task_done()으로 get 작업이 완료되었음을 표시해줘야 join()이 완료됨
    queue.join()
    logging.debug("tasks are done")
    # queue join() 은 완료되었지만 worker1의 while 문이 종료되지 않아 그 다음으로 진행하지 못하고 있다. break 조건인 None 을 넣어줘야 t1 쓰레드가 종료문까지 진행 가능
    queue.put(None)
    # t1 쓰레드가 종료되기를 기다림
    t1.join()
