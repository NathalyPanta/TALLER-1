from empresa import Empresa
from muestra import  Mostrar, Detalle
from usuario import Cliente, Coach
from helpers import Helper
import os

helper = Helper()
lista = ["\033[1;36m"+"1. Coach ","2. Cliente ","3. Salir"+"\033[0m"]
opcion = ""
while opcion !="3":
  os.system("cls")
  opcion =helper.menu(lista,"\033[1;33m" + "→→ USUARIOS " +"\033[0m")
  os.system("cls")
  if opcion == '2':
    opc1 = ""
    while opc1 != '2':
      os.system("cls")
      #print("\033[1;33m" + "⋯"*20 +"\033[0m")
      opc1 = helper.menu(["\033[1;36m"+"1) Rutinas", "2) Salir"+"\033[0m"], "\033[1;33m" +"▶ MODULOS"+"\033[0m")
      os.system("cls")
      if opc1 == "1":
        print("\033[1;33m" +"▶ RUTINAS"+"\033[0m")
        emp1= Empresa("0999999999", "SpaceWalker", "0928819085", "Durán", "spcwlk@gmail.com")
        usu = Cliente("Nat", "0928819085", "0959690781","nathypanta@hotmail.com","Durán", "727", True)
        mos = Mostrar(usu, "Cliente")
        mos.agregarDetalle("mancuernas", "20 minutos", "4 series")
        mos.agregarDetalle("zancadas", "10 minutos", "4 series")  
        mos.agregarDetalle(nombre, tiempo, serie)
        mos.mostrarInfo(emp1.razonsocial, emp1.ruc)
        input("\033[1;32m"+"\n"
          "Presiona una tecla para continuar..." +"\033[0m")
      elif opc1 == "2":
        input("\033[1;32m"+"Saliendo..." 
            "\n" "Presione una tecla para continuar..." +"\033[0m")
        break
  
  elif opcion == '1':
    opc1 = ""
    while opc1 != '3':
      os.system("cls")
      #print("✦"*20,"MODULOS","✦"*20)
      opc1 = helper.menu(["\033[1;36m"+"1) Rutinas","2) Añadir Rutina" ,"3) Salir"+"\033[0m"], "\033[1;33m" +"▶ MODULOS"+"\033[0m")
      os.system("cls")
      if opc1 == "1":
        print("\033[1;33m" +"▶ RUTINAS"+"\033[0m")
        emp1= Empresa("0999999999", "SpaceWalker", "0928819085", "Durán", "spcwlk@gmail.com")
        usu = Coach("Nat", "0928819085", "0959690781","nathypanta@hotmail.com","Durán", "727", True)
        mos = Mostrar(usu, "Coach") 
        mos.agregarDetalle("mancuernas", "20 min", "4 series")
        mos.agregarDetalle("zancadas", "20 min", "4 series")
        mos.agregarDetalle(nombre, tiempo, serie)
        mos.mostrarInfo(emp1.razonsocial, emp1.ruc)
        input("\033[1;32m"+"\n"
          "Presiona una tecla para continuar..." +"\033[0m")
      elif opc1 == "2":
        print("\033[1;33m" +"▶ AÑADIR RUTINAS"+"\033[0m")
        nombre =input("\033[1;36m"+"Ingrese nombre de rutina: " +"\033[0m")
        tiempo =input("\033[1;36m"+"Ingrese tiempo de rutina: " +"\033[0m")
        serie =input("\033[1;36m"+"Ingrese serie de rutinas: " +"\033[0m")
        usu = Coach("Nat", "0928819085", "0959690781","nathypanta@hotmail.com","Durán", "727", True)
        usu = Mostrar(usu, "Coach")
        usu.agregarDetalle(nombre, tiempo, serie)
      elif opc1 == "3":
        input("\033[1;32m"+"Saliendo..." 
            "\n" "Presione una tecla para continuar..." +"\033[0m")
        break
  
  elif opcion == "3":
    print("\033[1;33m"+"¡Gracias por visitarnos!" +"\033[0m")

    #"\033[1;32m"+ +"\033[0m"