import os
from clases.producto import Producto 
from clases.catalogo import Catalogo



def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')



class Usuario:
    def __init__(self,rut,nombre,apellido,tipo_usuario):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_usuario = tipo_usuario

    def menu(self):
        pass    


class Admin(Usuario):
    def __init__(self, rut, nombre, apellido, tipo_usuario):
        super().__init__(rut, nombre, apellido, tipo_usuario)

    def menu_admin(self,mi_productos):
     while True:
        
        print("==========================================")
        print("        PANEL DE ADMINISTRACIÓN")
        print("==========================================")
        print("1- Ver Catalogo")
        print("2- Agregar nuevo producto")
        print("3- Actualizar productos")
        print("4- Eliminar producto")
        print("5- <-- Volver al Menú Principal")
        print("------------------------------------------")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            limpiar_pantalla()
            print("==========================================")
            print("                CATALOGO")
            print("==========================================")
            mi_productos.abrir_catalogo()
            mi_productos.listar_catalogo()
            input("\nPresione Enter para volver al menú...") 

        elif opcion =="2":
            limpiar_pantalla()
            print("==========================================")
            print("         AGREGAR NUEVO PRODUCTO")
            print("==========================================")
            cod_prod = input("Ingrese ID del producto:")
            nom_prod = input("Ingrese Nombre del producto:")
            cat_prod = input("Ingrese categoria:")
            pre_prod = input("Ingrese precio:")
            stock_prod = input("Ingrese Stock del producto:")
            print("==========================================")
            opcion = input("\nPresione Y para guardar el producto:") 
            if opcion == "Y":
                producto= Producto(cod_prod,nom_prod,cat_prod,pre_prod,stock_prod)
                mi_productos.agregar_producto(producto)
                mi_productos.guardar_catalogo()
            else:
                print("Producto no guardado")

        elif opcion =="3":
            limpiar_pantalla()
            print("==========================================")
            print("          ACTUALIZAR PRODUCTOS")
            print("==========================================")
            mi_productos.abrir_catalogo()
            mi_productos.listar_catalogo()
            opcion_mod = input("Escriba ID del producto a modificar:")
            #cod_prod = input("Ingrese ID del producto:")
            nom_prod = input("Ingrese Nombre del producto:")
            cat_prod = input("Ingrese categoria:")
            pre_prod = input("Ingrese precio:")
            stock_prod = input("Ingrese Stock del producto:")
            print("==========================================")
            opcion2 = input("\nPresione Y para guardar el producto:") 
            if opcion2 == "Y":
                modificar = mi_productos.actualizar_producto(opcion_mod,nom_prod,cat_prod,pre_prod,stock_prod)
                if modificar:
                    print("\nProducto actualizado y guardado correctamente.")
                else:
                 print("\n Error: No se encontró un producto con ese ID.")
            else:
                print("Producto no guardado")

        elif opcion =="4":
            limpiar_pantalla()
            print("==========================================")
            print("           ELIMINAR PRODUCTO")
            print("==========================================")
            mi_productos.abrir_catalogo()
            mi_productos.listar_catalogo()
            opcion_eli = input("Escriba ID del producto a eliminar:")
            mi_productos.eliminar_producto(opcion_eli)

            input("\nPresione Enter para volver al menú...")

        elif opcion =="5":
            limpiar_pantalla()
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input()

    


class Cliente(Usuario):
    def __init__(self, rut, nombre, apellido, tipo_usuario):
        super().__init__(rut, nombre, apellido, tipo_usuario)

    def menu_cliente(self,mi_productos):
    
       while True:
            print("==========================================")
            print("        PANEL DE CLIENTE")
            print("==========================================")
            print("1- Ver catalogos de productos:")
            print("2- Buscar productos:")
            print("3- Agregar productos al carro:")
            print("4- Ver carro:")
            print("5- confirmar compra:")
            print("6- <-- Volver al Menú Principal")

            opcion= input("Ingrese una opcion: ")
            if opcion == "1":
                limpiar_pantalla()
                mi_productos.listar_catalogo()
                input("\nPresione Enter para continuar...")
            elif opcion =="2":
                limpiar_pantalla()
                mi_productos.abrir_catalogo()
                msj=input("Ingrese Nombre o categoria del producto a buscar:")
                mi_productos.buscar_producto(msj)
                input("\nPresione Enter para continuar...")
            elif opcion == "6":
                break




