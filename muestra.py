from empresa import Empresa
from usuario import Cliente, Coach
from interface import RutinaCoach
# import os

class Detalle:
  _NumeroR = 0
  def __init__(self, rutina,tiempo, serie):
    Detalle._NumeroR += 1
    self.linea = Detalle._NumeroR
    self.rutina = rutina
    self.tiempo = tiempo
    self.serie = serie

class Mostrar: 
  _NumeroR = 0
  def __init__(self, usuario, rol):
    Detalle._NumeroR += 1
    self.usuario = usuario
    self.rol = rol
    self.detalleR = []
  
  def agregarDetalle(self, rutinas, tiempos, series):
    detalle = Detalle(rutinas,tiempos,series)
    self.detalleR.append(detalle)

  def mostrarInfo(self, empNom, empRuc):
    print("Empresa: {:17} Ruc:{}".format(empNom, empRuc))
    self.usuario.mostrarUsuario()
    print("Rol: {}".format(self.rol))
    print("\033[1;33m"+" "*15,"> Lista de rutinas <"," "*20 +"\033[0m")
    print("\033[1;36m"+"NumeroR    Ejercicio         Tiempo        Serie" +"\033[0m")
    for det in self.detalleR:
      print("{:7} {:16} {:10} {:5}".format(det.linea, det.rutina, det.tiempo, det.serie))


if __name__ == "__main__":
  emp1= Empresa("0999999999", "SpaceWalker", "0928819085", "Durán", "spcwlk@gmail.com")
  usu = Cliente("Nat", "0928819085", "0959690781","nathypanta@hotmail.com","Durán", "727", True)
  usua = Coach("Nat", "0928819085", "0959690781","nathypanta@hotmail.com","Durán", "727", True)
  mos = Mostrar(usua, "Coach")
  nombre =input("Ingrese nombre de rutina: ")
  tiempo =input("Ingrese tiempo de rutina: ")
  serie =input("Ingrese serie de rutinas: ")
  # usu = RutinaCoach()
  # usu.añadirRutina(nombre, tiempo, serie)
  mos.agregarDetalle(nombre, tiempo, serie)
  mos.agregarDetalle("mancuernas", "20 minutos", "4 series")
  mos.agregarDetalle("zancadas", "20 minutos", "4 series")
  mos.mostrarInfo(emp1.razonsocial, emp1.ruc)