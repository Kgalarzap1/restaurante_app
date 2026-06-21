# Sistema de Gestión de Restaurante - POO en Python

Estudiante:Kleber Galarza

## Descripción del sistema

Este proyecto implementa un sistema básico de gestión de un restaurante
utilizando Programación Orientada a Objetos (POO) en Python. El sistema
permite registrar productos del menú (platos, bebidas, postres) y
clientes, además de simular pedidos realizados por los clientes.

El objetivo no es construir una aplicación completa con menú interactivo,
sino demostrar el uso correcto de clases, objetos, constructores,
atributos, métodos, el método especial `__str__()` y la organización
modular de un proyecto Python mediante importaciones entre archivos.

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── producto.py     # Clase Producto: representa un ítem del menú
│   └── cliente.py      # Clase Cliente: representa a un cliente y sus pedidos
├── servicios/
│   └── restaurante.py  # Clase Restaurante: administra productos y clientes
└── main.py              # Punto de arranque del programa
```

- **modelos/producto.py**: define la clase `Producto`, con atributos como
  nombre, categoría, precio y disponibilidad, y métodos para cambiar su
  estado o aplicar descuentos.
- **modelos/cliente.py**: define la clase `Cliente`, con atributos como
  nombre, cédula y teléfono, además de su lista de pedidos y el cálculo
  del total a pagar.
- **servicios/restaurante.py**: define la clase `Restaurante`, encargada
  de administrar las listas de productos y clientes, y de mostrar la
  información registrada en consola.
- **main.py**: crea los objetos `Producto`, `Cliente` y `Restaurante`,
  los relaciona entre sí y ejecuta el programa, mostrando los resultados
  en consola.

## Cómo ejecutar el programa

```bash
cd restaurante_app
python3 main.py
```

## Reflexión sobre modularidad

Organizar el software en módulos separados (modelos, servicios y punto
de ejecución) permite que cada archivo tenga una responsabilidad clara
y específica. Esto facilita el mantenimiento del código, ya que un
cambio en la lógica de negocio (por ejemplo, en `Restaurante`) no afecta
la definición de las entidades (`Producto`, `Cliente`), y viceversa.
Además, separar responsabilidades hace que el proyecto sea más legible,
escalable y fácil de probar, ya que cada clase puede analizarse y
modificarse de forma independiente sin afectar al resto del sistema.
