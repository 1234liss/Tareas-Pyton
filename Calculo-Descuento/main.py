def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a un monto total.

    Args:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float): El porcentaje de descuento a aplicar (por defecto, 10%).

    Returns:
        float: El monto del descuento calculado.
    """
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento


if __name__ == "__main__":
    monto_compra1 = 100.0
    descuento1 = calcular_descuento(monto_compra1)
    monto_final1 = monto_compra1 - descuento1

    print(f"Monto de la compra: ${monto_compra1:.2f}")
    print(f"Descuento aplicado: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}")

    monto_compra2 = 250.0
    porcentaje_descuento2 = 20
    descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
    monto_final2 = monto_compra2 - descuento2

    print(f"\nMonto de la compra: ${monto_compra2:.2f}")
    print(f"Descuento aplicado: ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")