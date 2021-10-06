#!/usr/bin/python3

from multiprocessing import Process
import subprocess
from pa import pa
from pb import pb
from pc import pc

import os

def wpa():
  ipa = pa()
  print(os.getpid())
  print(f'a={os.getpid()}')
  ipa.loop = True
  ipa.countloop()

def wpb():
  ipb = pb()
  print(f'b={os.getpid()}')
  ipb.loop = True
  ipb.countloop()

def wpc():
  ipc = pc()
  print(f'c={os.getpid()}')
  ipc.loop = True
  ipc.countloop()

def wpn(command):
  ppa = subprocess.run(command, shell=True)

def call_by_Process():
  print('creating pa')
  ppa = Process(target=wpa)
  ppa.start()
  print('pa is started', ppa.is_alive())
  print('creating pb')
  ppb = Process(target=wpb)
  ppb.start()
  print('pb is started', ppb.is_alive())
  print('creating pc')
  ppc = Process(target=wpc)
  ppc.start()
  print('pc is started', ppc.is_alive())
  ppa.join()
  print('pa is finished', ppa.is_alive())
  ppb.join()
  print('pb is finished', ppb.is_alive())
  ppc.join()
  print('pc is finished', ppc.is_alive())

def call_by_subprocess_run():
  import time
  print('creating pa')
  ppa = subprocess.run('python3 pa.py &', shell=True)
  print('creating pb')
  ppb = subprocess.run('python3 pb.py &', shell=True)
  print('creating pc')
  ppc = subprocess.run('python3 pc.py &', shell=True)
  time.sleep(20)

def call_by_Process_and_subprocess_run():
  print('creating pa')
  ppa = Process(target=wpn, args=(CMD_A,))
  ppa.start()
  print('creating pb')
  ppb = Process(target=wpn, args=(CMD_B,))
  ppb.start()
  print('creating pc')
  ppc = Process(target=wpn, args=(CMD_C,))
  ppc.start()
  ppa.join()
  print('pa finished')
  ppb.join()
  print('pb finished')
  ppc.join()
  print('pc finished')

CMD_A = 'python3 pa.py'
CMD_B = 'python3 pb.py'
CMD_C = 'python3 pc.py'

if __name__ == '__main__':
  print(f'parent={os.getpid()}')

  call_by_Process()
  #call_by_subprocess_run()
  #call_by_Process_and_subprocess_run()