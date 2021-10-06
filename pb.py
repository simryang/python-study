#!/usr/bin/python3
import os

class pb():
  def __init__(self):
    self.n = 0
    self.loop = False

  def countloop(self):
    while self.loop:
      self.n += 1
    self.result()

  def result(self):
    print(f'result of pb = {self.loop}')

if __name__ == '__main__':
  ipb = pb()
  print(f'b={os.getpid()}')
  ipb.loop = True
  ipb.countloop()