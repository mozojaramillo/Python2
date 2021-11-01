import Producto
import store


tienda1 = store.Tienda("tienda1")
tienda2 = store.Tienda("tienda2")

tomates = Producto.Producto("Tomate", 1000, "Verduras", 100)
leche = Producto.Producto("leche", 800, "despensa", 101)

tomates.print_info()