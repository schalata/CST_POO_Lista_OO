class TV:

  def __init__(self, canal = 0, volume = 0): 
    self._canal = canal
    self._volume = volume

  def __str__(self):
    return f'canal = {self._canal}, volume = {self._volume}'

  def mutar(self):
    self._volume = 0

  def alterar_volume(self, volume):
    self._volume = volume

  def aumentar_volume(self):
    self._volume += 1

  def diminuir_volume(self):
    self._volume -= 1

  def trocar_canal(self, canal):
    self._canal = canal

  def aumentar_canal(self):
    self._canal += 1

  def diminuir_canal(self):
    self._canal -= 1

  def get_canal(self):
    return self._canal

  def get_volume(self):
    return self._volume