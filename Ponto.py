from math import sqrt, pow

class Ponto:

  def __init__(self, x = 0, y = 0): 
    self._x = x
    self._y = y

  def __str__(self):
    return f'x = {self._x}, y = {self._y}'

  def resetar(self):
    self._x, self._y = 0, 0

  def mover(self, x, y):
    self._x, self._y = x, y

  def get_x(self):
    return self._x

  def get_y(self):
    return self._y

  def forneca_distancia(self, ponto):
    dx = abs(self._x - ponto.get_x())
    dy = abs(self._y - ponto.get_y())
    return sqrt(pow(dx, 2) + pow(dy, 2))