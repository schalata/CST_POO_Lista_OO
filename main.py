#from BombaAgua import BombaAgua
#from Calculadora import Calculadora
#from TV import TV
#from Ponto import Ponto
from Quadrado import Quadrado

if __name__ == '__main__':

  ########## Ex. 01 e 02 ##########
  
  q1 = Quadrado(7)
  q2 = Quadrado(4)

  print(q1)

  q2 = Quadrado(4)
  print(q2)

  print(q1.compara_area(q2))
  
  ########## Ex. 03 ##########

  # tv = TV()
  # print(tv)
  # tv.alterar_volume(10)
  # tv.trocar_canal(13)
  # print(tv)
  # tv.aumentar_volume()
  # tv.diminuir_canal()
  # print(tv)

  ########## Ex. 04 e 05 ##########

  # p1 = Ponto()
  # print(p1)
  # p2 = Ponto(3, 4)
  # print(p2)
  # print(p1.forneca_distancia(p2))

  ########## Ex. 06 ##########
  
  # b = BombaAgua();
  # print(b)
  # tempo = 5
  # print(f"Bomba d\'água ligada por {tempo} s.")
  # b.ligar(tempo)  
  # b.desligar()
  # print("Bomba desligada!")

  ########## Ex. 07 ##########
  
  # c = Calculadora();
  
  # opcao=1

  # while opcao != 6:
  #   print("#" * 30)
  #   print("1. Alterar os valores a e b")  
  #   print("2. Somar")
  #   print("3. Subtrair")
  #   print("4. Multiplicação")
  #   print("5. Divisão ")
  #   print("6. Sair")
  #   print("#" * 30)

  #   opcao = int(input("Opção: "))

  #   if(opcao==1):
  #     a = int(input("Digite o 1o valor: "))
  #     c.set_a(a)
  #     b= int(input("Digite o 2o valor: "))
  #     c.set_b(b)
  #   elif(opcao==2):      
  #     print(f'Resultado = {c.somar()}')
  #   elif(opcao==3):
  #     print(f'Resultado = {c.subtrair()}')
  #   elif(opcao==4):
  #     print(f'Resultado = {c.multiplicar()}')
  #   elif(opcao==5):
  #     print(f'Resultado = {c.dividir()}')

  