class Rutina():
  def añadirRutina(self):
    pass
  def mostrarRutina(self):
    pass
 
class RutinaCoach():
  def añadirRutina(self, nombre, tiempo, serie):
    print(" "*15,"Ingreso de rutinas"," "*20)
    self.nombre = nombre
    self.tiempo = tiempo
    self.serie = serie
  def mostrarRutina(self):
    print(" "*15,"Rutinas ingresadas"," "*20)
    return("Rutinas: {} Tiempo: {} Series: {}".format(self.nombre, self.tiempo, self.serie))

class RutinaCliente():
  def mostrarRutina(self):
    print(" "*15,"Rutinas ingresadas"," "*20)
    return("Rutinas: {} Tiempo: {} Series: {}".format(self.nombre, self.tiempo, self.serie))

if __name__ == "__main__":
  usu = RutinaCoach()
  usu.añadirRutina()
  usu.mostrarRutina()