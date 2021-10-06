#!/usr/bin/python3

import time
import concurrent.futures

def func1():
    while True:
        print("func1")
        time.sleep(1)


def func2():
    while True:
        print("func2")
        time.sleep(1)


def func(value = 0):
    while True:
        print(f"func{value}")
        time.sleep(1)

MAXWORKERS=200
if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=MAXWORKERS)
    executor.submit(func1)
    executor.submit(func2)
    executor_test = concurrent.futures.ThreadPoolExecutor(max_workers=MAXWORKERS)
    for i in range(MAXWORKERS):
        if i is not 1 and i is not 2:
            executor_test.submit(func, i)