class Usuario:
    def __init__(self,rut,nombre,apellido,tipo_usuario):
        self.rut = rut
        self.nombre = nombre
        self.nombre = apellido
        self.tipo_usuario = tipo_usuario


class Admin(Usuario):
    def __init__(self, rut, nombre, apellido, tipo_usuario):
        super().__init__(rut, nombre, apellido, tipo_usuario)

    


class Cliente(Usuario):
    def __init__(self, rut, nombre, apellido, tipo_usuario):
        super().__init__(rut, nombre, apellido, tipo_usuario)

    


class Producto:
    def __init__(self,id,nombre,categoria,precio):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio


class Catalogo:
    def __init__(self):
        self.producto = []

        
    def agregar_producto(self,producto):
        self.producto.append(producto)



    def listar_catalogo(self):
        for producto in self.productos:
         print(producto)

    def eliminar_producto():
        pass