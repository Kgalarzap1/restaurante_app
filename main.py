"""
Módulo: main.py
Punto de arranque del programa. Aquí se crean los objetos
y se demuestra el funcionamiento del sistema de restaurante.
"""

# Importaciones desde los módulos del proyecto
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    # Creamos el restaurante principal
    restaurante = Restaurante("La Buena Mesa")

    # Creamos algunos productos
    p1 = Producto("Seco de pollo", "plato fuerte", 4.50)
    p2 = Producto("Jugo de mora", "bebida", 1.50)
    p3 = Producto("Flan de caramelo", "postre", 2.00)

    # Agregamos los productos al restaurante
    restaurante.agregar_producto(p1)
    restaurante.agregar_producto(p2)
    restaurante.agregar_producto(p3)

    # Creamos un cliente
    cliente1 = Cliente("Alexander Toapanta", "1750000000")

    # El cliente realiza pedidos
    cliente1.realizar_pedido(p1)
    cliente1.realizar_pedido(p2)

    # Registramos al cliente en el restaurante
    restaurante.agregar_cliente(cliente1)

    # Mostramos la información del sistema
    restaurante.mostrar_menu()
    restaurante.mostrar_clientes()

    print(f"\n{restaurante}")


if __name__ == "__main__":
    main()
