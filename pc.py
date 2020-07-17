#!/usr/bin/python3
import os

class pc():
  def __init__(self):
    self.n = 0
    self.loop = False

  def countloop(self):
    while self.loop:
      self.n += 1
    self.result()

  def result(self):
    print(f'result of pc = {self.loop}')


if __name__ == '__main__':
  ipc = pc()
  print(f'c={os.getpid()}')
  ipc.loop = True
  ipc.countloop()