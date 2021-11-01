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

