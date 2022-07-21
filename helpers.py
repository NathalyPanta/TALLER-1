import os
os.system("cls")
class Calculo:
  pass

class Helper:
  def __init__(self):
    x=10
    pass
  def menu(self,opciones, titulo):
    print(titulo)
    for opcion in opciones:
      print(opcion)
    literal = input("\033[3;35m"+"Elija una opcion de [1 a {}]: ".format(len(opciones))+"\033[0m")
    return literal