class Usuario:
    def __init__(self,rut,nombre,apellido,tipo_usuario):
        self.rut = rut
        self.nombre = apellido
        self.tipo_usuario = tipo_usuario


class Admin(Usuario):
    def __init__(self, rut, nombre, apellido, tipo_usuario):
        super().__init__(rut, nombre, apellido, tipo_usuario)

    def listar_productos():
        pass

    def crear_producto():
        pass
    def actualizar_producto():
        pass
    def eliminar_producto():
        pass
    def guardar_catalogo():
        pass    
            


class Cliente(Usuario):
    def __init__(self, rut, nombre, apellido, tipo_usuario):
        super().__init__(rut, nombre, apellido, tipo_usuario)

    def ver_catalogo():
        pass

    def buscar_producto():
        pass

    def agregar_pro_carrito():
        pass

    def ver_carrito():
        pass

    def confirmar_compra():
