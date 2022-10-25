from time import sleep

class BombaAgua:
  
  def __init__(self):
    self._status = False

  def __str__(self):
    return f'status = {self._status}'

  def ligar(self, tempo):
    self._status = True
    sleep(tempo)

  def desligar(self):
    self._status = False
    