"""
Módulo: cliente.py
Contiene la clase Cliente, que representa a una persona que
realiza o consume un pedido en el restaurante.
"""


class Cliente:
    """Representa a un cliente registrado en el restaurante."""

    def __init__(self, nombre, cedula, telefono=None):
        # Atributos principales del cliente
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.pedidos = []  # Lista de productos pedidos por el cliente

    def realizar_pedido(self, producto):
        """Agrega un producto a la lista de pedidos del cliente."""
        self.pedidos.append(producto)

    def total_pedidos(self):
        """Calcula el total a pagar según los productos pedidos."""
        return sum(p.precio for p in self.pedidos)

    def __str__(self):
        # Representación legible del cliente en consola
        return (f"Cliente: {self.nombre} | Cédula: {self.cedula} | "
                f"Pedidos: {len(self.pedidos)} | Total: ${self.total_pedidos():.2f}")
