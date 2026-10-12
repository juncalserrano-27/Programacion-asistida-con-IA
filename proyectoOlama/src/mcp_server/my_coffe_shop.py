

from fastmcp import FastMCP

mcp = FastMCP("CafeteriaServer")

MENU_CAFETERIA = {
    "latte vainilla": {"precio": 55.00, "categoria": "Bebidas calientes", "descripcion": "Café espresso con leche vaporizada y jarabe de vainilla."},
    "cappuccino": {"precio": 50.00, "categoria": "Bebidas calientes", "descripcion": "Espresso, leche vaporizada y abundante espuma."},
    "cold brew": {"precio": 60.00, "categoria": "Bebidas frías", "descripcion": "Café infusionado en frío durante 12 horas."},
    "matcha latte": {"precio": 65.00, "categoria": "Bebidas frías", "descripcion": "Té matcha ceremonial con leche cremosa."},
    "croissant de mantequilla": {"precio": 42.00, "categoria": "Panadería", "descripcion": "Croissant horneado del día, crujiente y hojaldrado."},
    "pastel de zanahoria": {"precio": 58.00, "categoria": "Postres", "descripcion": "Rebanada con frosting de queso crema y nueces."}
}

PEDIDOS_SIMULADOS = {
    "CAF-001": "Preparando bebida en barra",
    "CAF-002": "Listo para recoger en barra",
    "CAF-003": "Entregado con éxito"
}

@mcp.tool()
def obtener_menu_cafeteria() -> str:
    """
    Muestra la lista completa del menú de la cafetería, incluyendo bebidas, panadería y postres con sus precios.
    Use esta herramienta cuando el usuario quiera ver el menú o los productos disponibles.

    Resultado que regresa: el menu de la cafeteria
    """
    resultado = "☕ MENÚ DE LA CAFETERÍA:\n" + "="*30 + "\n"
    for producto, info in MENU_CAFETERIA.items():
        resultado += f"• {producto.title()} ({info['categoria']}) - ${info['precio']:.2f} MXN\n  Descripción: {info['descripcion']}\n\n"
    return resultado


@mcp.tool()
def consultar_estado_pedido(id_pedido: str) -> str:
    """
    Consulta el estado actual de un pedido en curso en la cafetería.
    
    Args:
        id_pedido: El código identificador del pedido (ej. 'CAF-001').
    """
    estado = PEDIDOS_SIMULADOS.get(id_pedido.upper(), "No se encontró ningún pedido con ese código en el sistema.")
    return f"Estado del pedido {id_pedido.upper()}: {estado}."


@mcp.tool()
def calcular_total_pedido(lista_productos: str) -> str:
    """
    Calcula el costo total de los productos de la cafetería que el cliente desea comprar.
    
    Args:
        lista_productos: Nombres de los productos separados por comas (ej. 'cappuccino, croissant de mantequilla').
    """
    items = [item.strip().lower() for item in lista_productos.split(",")]
    total = 0.0
    detalle = "🧾 Resumen de tu pedido:\n"
    
    for item in items:
        if item in MENU_CAFETERIA:
            precio = MENU_CAFETERIA[item]["precio"]
            total += precio
            detalle += f"- {item.title()}: ${precio:.2f} MXN\n"
        else:
            detalle += f"- {item} (No disponible en el menú de la cafetería)\n"
            
    detalle += f"\nTotal a pagar: ${total:.2f} MXN"
    return detalle


@mcp.tool()
def consultar_horarios_y_ubicacion() -> str:
    """
    Informa los horarios de servicio y la ubicación física de la sucursal de la cafetería.
    """
    return "📍 Ubicación: Av. Juárez #405, Centro. Horarios: Lunes a Sábado de 7:00 AM a 9:00 PM, Domingos de 8:00 AM a 6:00 PM."


@mcp.tool()
def ver_promociones_dia() -> str:
    """
    Muestra las promociones y descuentos especiales vigentes en la cafetería.
    """
    return "🎉 ¡Promoción del día! En la compra de cualquier bebida grande, llévate un Croissant de mantequilla con 50% de descuento."


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8080)