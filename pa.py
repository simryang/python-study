#!/usr/bin/python3
import os

class pa():
  def __init__(self):
    self.n = 0
    self.loop = False

  def result(self):
    print(f'result of pa = {self.loop}')

  def countloop(self):
    while self.loop:
      self.n += 1
    self.result()

if __name__ == '__main__':
  ipa = pa()
  print(os.getpid())
  print(f'a={os.getpid()}')
  ipa.loop = True
  ipa.countloop()