import random

def ingresar_stock():
    stock = {}
    while True:
        codigo = input("Ingrese el código del producto (1000-9999) o presione enter para finalizar: ")
        if not codigo:
            break
        codigo = int(codigo)
        if codigo < 1000 or codigo > 9999 or codigo in stock:
            print("Ingrese un código válido y no repetido.")
            continue
        stock[codigo] = random.randint(0, 100)
    return stock

def listar_stock(stock):
    print("Listado completo por Código del producto, nombre y cantidad en stock:")
    for codigo, cantidad in sorted(stock.items()):
        print(f"Código: {codigo}, Stock: {cantidad}")

def stock_menor_minimo(stock, min_stock=5):
    print("Código del producto por debajo del stock mínimo:")
    for codigo, cantidad in stock.items():
        if cantidad < min_stock:
            print(codigo)

def mayor_cantidad_en_stock(stock):
    max_cantidad = max(stock.values())
    productos_max_cantidad = [codigo for codigo, cantidad in stock.items() if cantidad == max_cantidad]
    
    print(f"Mayor cantidad en stock: {max_cantidad}")
    print("Códigos de productos con la mayor cantidad en stock:")
    for codigo in productos_max_cantidad:
        print(codigo)

def main():
    stock = ingresar_stock()

    listar_stock(stock)
    stock_menor_minimo(stock)
    mayor_cantidad_en_stock(stock)

if __name__ == "__main__":
    main()