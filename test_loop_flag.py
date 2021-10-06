import time
import threading

class testthread(threading.Thread):
  def __init__(self, testvar=None):
    threading.Thread.__init__(self)
    self.enabled = False
    
  def stop(self):
    self.enabled = False
 
  def enable(self):
    self.enabled = True

  def run(self):
    try:
      while self.enabled:
        kkk='kkk'
      time.sleep(0.1)
    except Exception as e:
      pass

if __name__ == '__main__':
  ttest = testthread('abcd')
  ttest.enable()
  ttest.start()
  import subprocess
  output = subprocess.check_output('ps -ax').decode('utf-8')
  print(output)
  time.sleep(0.001)
  ttest.stop()