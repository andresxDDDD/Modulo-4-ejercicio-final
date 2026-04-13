from menu.menu import menu_principal,limpiar_pantalla
""" from funciones.mostrar_catalogo import ver_productos, buscar_producto
from productos.catalogo import catalogo
from carrito.agregar_carrito import agrega_producto,calcular_total,mostrar_carrito,vaciar_carrito

 """
def main():
    carr_prod =[]
    ejecutar= True
    while ejecutar:
        limpiar_pantalla()
        ejecutar=menu_principal()


main()    