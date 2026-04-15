
from clases.producto import Producto

class Carrito():
   def __init__(self):
      self.items = {}

   def __str__(self):
      return f"{self.items}"   

   def agregar_carrito(self,producto,cantidad):
      if producto in self.items:
         self.items["producto"]+= cantidad
      else:
         self.items["producto"]= cantidad

   def ver_carrito(self):
      total=0
      for p,c  in self.items.items():
         subtotal = p.precio * c
         total += subtotal  
         print(f"{p.nombre}- cantidad{c}-subtotal{subtotal}")   
      print(f"total de la compra:{total}")    
            
   def calcular_total(self):
        return 


   def vaciar_carrito(self):
     self.items.clear()  
