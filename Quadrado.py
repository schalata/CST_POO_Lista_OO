class Quadrado:
  def __init__(self, lado = 1): 
    self._lado = lado
    self._area = self._lado * self._lado
    self._perimetro = 4 * self._lado

  # Imprimindo os atributos com __str__
  def __str__(self):
    return f'lado = {self._lado}, area = {self._area}, perimetro = {self._perimetro}'
    
  # lado.setter
  def set_lado(self, lado):
    self._lado = lado
    self._area = self._lado * self._lado
    self._perimetro = 4 * self._lado

  # Fornece o lado
  def get_lado(self):
    return self._lado

  # Fornece a área
  def get_area(self):
    return self._area

  # Fornece o perímetro
  def get_perimetro(self):
    return self._perimetro

  # Compara o quadrado com outro objeto instanciado da mesma classe
  def compara_area(self, quadrado):
    if self._area > quadrado.get_area():
      return 'Maior'
    elif self._area < quadrado.get_area():
      return 'Menor'
    else:
      return 'Igual'
  