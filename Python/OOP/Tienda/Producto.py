class Producto:
    def __init__(self, nombre, precio, categoria, id):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.id = id
    
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

