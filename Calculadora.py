class Calculadora:
  
  def __init__(self):
    self._a = 0
    self._b = 0

  def __str__(self):
    return f'a = {self._a}, b = {self._b}'

  def set_a(self, a):
    self._a = a

  def set_b(self, b):
    self._b = b  
 
  def somar(self):
    return self._a + self._b

  def subtrair(self):
    return self._a - self._b

  def multiplicar(self):
    return self._a * self._b

  def dividir(self):
    try:
      return self._a / self._b
    except:
      print("Uma exceção ocorreu!")