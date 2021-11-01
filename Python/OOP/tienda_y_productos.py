class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def add_product(self, producto_nuevo):
        self.productos.append(producto_nuevo)

        return self

    def sell_product(self, id):
        self.productos.pop(id)
        print(self.print_info)

        return self

    def inflation(self, inflacion):
        for i in self.productos:
            i.update_price(inflacion)

        return self
    def set_clearence(self, categoria, descuento_porcentual):
        for i in self.productos:
            if i.categoria == categoria:
                i.update_price(descuento_porcentual, False)
        
        return self


class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def update_price(self, cambio_porcentual, sube = True):
        if sube == True:
            self.precio = self.precio*(1 + cambio_porcentual)
        else:
            self.precio = self.precio*(1 - cambio_porcentual)

        return self

    def print_info(self):
        print (f"El nombre del producto es: {self.nombre}")
        print(f"{self.nombre} es de la catergoría {self.categoria}")
        print(f"El precios de {self.nombre} es de {self.precio}")

        return self


tienda1 = Tienda("tienda1")
tienda2 = Tienda("tienda2")

tomates = Producto("Tomate", 1000, "Verduras")
leche = Producto("leche", 800, "despensa")

tomates.print_info()

tienda1.add_product(tomates)
tienda1.add_product(leche)

tienda2.add_product(tomates)
tienda2.add_product(leche)

print(tienda1.productos[0].print_info())