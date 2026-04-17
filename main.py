
from clases.catalogo import Catalogo
from clases.usuario import Admin, Cliente


class Tienda:
        def __init__(self):
            self.catalogo = Catalogo()
            self.catalogo.abrir_catalogo()

   

        def iniciar(self):

         while True:
                 
            print("==========================================")
            print("       SISTEMA DE ECOMMERCE ")
            print("==========================================")
            print("1. Ingresar como ADMINISTRADOR")
            print("2. Ingresar como CLIENTE")
            print("3. Salir")
            print("------------------------------------------")

            opcion = input("Seleccione el rol:")

            if opcion == "1":
                admin = Admin("16551814-4","Andres","Moraga","admin")
                admin.menu_admin(self.catalogo)

            elif opcion =="2":
                cliente = Cliente("16551814-4","Andres","Moraga","admin")
                cliente.menu_cliente(self.catalogo)
            else: 
                break


if __name__ == "__main__":
    tienda = Tienda()
    tienda.iniciar()