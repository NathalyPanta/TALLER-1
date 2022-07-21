class Empresa:
    def __init__(self,ruc, nombre, telf, dirc, correo):
        self.ruc = ruc
        self.razonsocial = nombre
        self.telf = telf
        self.dirc = dirc
        self.correo = correo

if __name__ == "__main__":
    emp1 = Empresa("042675158", "SpaceWalker", "0959690781", "Guayaquil", "abc@gmail.com")
    emp2 = Empresa("042675158", "BananaSlug", "0959690781", "Durán", "qwerty@hotmail.com")
    print(emp1.razonsocial, emp1.ruc)
    print(emp2.razonsocial, emp2.ruc)