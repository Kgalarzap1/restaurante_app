"""
Módulo: restaurante.py
Contiene la clase Restaurante, encargada de administrar
los productos y clientes registrados en el sistema.
"""


class Restaurante:
    """Gestiona las operaciones principales del restaurante."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []   # Lista de objetos Producto
        self.clientes = []    # Lista de objetos Cliente

    def agregar_producto(self, producto):
        """Registra un nuevo producto en el menú del restaurante."""
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        """Registra un nuevo cliente en el sistema."""
        self.clientes.append(cliente)

    def mostrar_menu(self):
        """Muestra en consola todos los productos disponibles."""
        print(f"\n--- Menú de {self.nombre} ---")
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        """Muestra en consola la información de todos los clientes."""
        print(f"\n--- Clientes de {self.nombre} ---")
        for cliente in self.clientes:
            print(cliente)

    def __str__(self):
        return (f"Restaurante {self.nombre} | "
                f"{len(self.productos)} productos | {len(self.clientes)} clientes")
