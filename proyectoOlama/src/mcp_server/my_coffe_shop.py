from fastmcp import FastMCP

mcp = FastMCP("CafeteriaServer")

COFFEE_SHOP_MENU = {
    "latte vainilla": {"precio": 55.00, "categoria": "Bebidas calientes", "descripcion": "Café espresso con leche vaporizada y jarabe de vainilla."},
    "cappuccino": {"precio": 50.00, "categoria": "Bebidas calientes", "descripcion": "Espresso, leche vaporizada y abundante espuma."},
    "cold brew": {"precio": 60.00, "categoria": "Bebidas frías", "descripcion": "Café infusionado en frío durante 12 horas."},
    "matcha latte": {"precio": 65.00, "categoria": "Bebidas frías", "descripcion": "Té matcha ceremonial con leche cremosa."},
    "croissant de mantequilla": {"precio": 42.00, "categoria": "Panadería", "descripcion": "Croissant horneado del día, crujiente y hojaldrado."},
    "pastel de zanahoria": {"precio": 58.00, "categoria": "Postres", "descripcion": "Rebanada con frosting de queso crema y nueces."}
}

SIMULATED_ORDERS = {
    "CAF-001": "Preparando bebida en barra",
    "CAF-002": "Listo para recoger en barra",
    "CAF-003": "Entregado con éxito"
}

@mcp.tool()
def get_coffee_shop_menu() -> str:
    """
    Muestra la lista completa del menú de la cafetería, incluyendo bebidas, panadería y postres con sus precios.
    Use esta herramienta cuando el usuario quiera ver el menú o los productos disponibles.

    Resultado que regresa: el menu de la cafeteria
    """
    result = "☕ MENÚ DE LA CAFETERÍA:\n" + "="*30 + "\n"
    for product, info in COFFEE_SHOP_MENU.items():
        result += f"• {product.title()} ({info['categoria']}) - ${info['precio']:.2f} MXN\n  Descripción: {info['descripcion']}\n\n"
    return result


@mcp.tool()
def check_order_status(order_id: str) -> str:
    """
    Consulta el estado actual de un pedido en curso en la cafetería.
    
    Args:
        order_id: El código identificador del pedido (ej. 'CAF-001').
    """
    status = SIMULATED_ORDERS.get(order_id.upper(), "No se encontró ningún pedido con ese código en el sistema.")
    return f"Estado del pedido {order_id.upper()}: {status}."


@mcp.tool()
def calculate_order_total(product_list: str) -> str:
    """
    Calcula el costo total de los productos de la cafetería que el cliente desea comprar.
    
    Args:
        product_list: Nombres de los productos separados por comas (ej. 'cappuccino, croissant de mantequilla').
    """
    items = [item.strip().lower() for item in product_list.split(",")]
    total = 0.0
    detail = "🧾 Resumen de tu pedido:\n"
    
    for item in items:
        if item in COFFEE_SHOP_MENU:
            price = COFFEE_SHOP_MENU[item]["precio"]
            total += price
            detail += f"- {item.title()}: ${price:.2f} MXN\n"
        else:
            detail += f"- {item} (No disponible en el menú de la cafetería)\n"
            
    detail += f"\nTotal a pagar: ${total:.2f} MXN"
    return detail


@mcp.tool()
def check_hours_and_location() -> str:
    """
    Informa los horarios de servicio y la ubicación física de la sucursal de la cafetería.
    """
    return "📍 Ubicación: Av. Juárez #405, Centro. Horarios: Lunes a Sábado de 7:00 AM a 9:00 PM, Domingos de 8:00 AM a 6:00 PM."


@mcp.tool()
def view_daily_promotions() -> str:
    """
    Muestra las promociones y descuentos especiales vigentes en la cafetería.
    """
    return "🎉 ¡Promoción del día! En la compra de cualquier bebida grande, llévate un Croissant de mantequilla con 50% de descuento."


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8080)
