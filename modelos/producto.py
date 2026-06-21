"""
Módulo: producto.py
Contiene la clase Producto, que representa un plato o bebida
disponible en el menú del restaurante.
"""


class Producto:
    """Representa un producto (plato o bebida) del restaurante."""

    def __init__(self, nombre, categoria, precio, disponible=True):
        # Atributos principales del producto
        self.nombre = nombre
        self.categoria = categoria      # ej: "plato fuerte", "bebida", "postre"
        self.precio = precio
        self.disponible = disponible

    def cambiar_disponibilidad(self, estado):
        """Permite marcar un producto como disponible o agotado."""
        self.disponible = estado

    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al precio del producto."""
        self.precio -= self.precio * (porcentaje / 100)

    def __str__(self):
        # Representación legible del producto en consola
        estado = "Disponible" if self.disponible else "Agotado"
        return f"{self.nombre} ({self.categoria}) - ${self.precio:.2f} - {estado}"
