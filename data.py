from datetime import datetime
import json
from random import randint

TAPIOCAS = {
    "banana": 15, "queijo com presunto": 12, "carne seca": 14,
    "chocolate": 15, "ovo": 12, "bacon": 13, 
    "carne seca c/catupiry": 15,"frango": 13,
    "frango c/catupiry": 14, "calabresa": 12,
}
HAMBURGUERES = {
    "x-tudo": 15, "x-bacon": 12, "x-egg": 11,
    "x-linguiça": 12, "x-gordinho": 14, "simples": 10,
    "x-salada": 11, "x-gordão": 22
}
BEBIDAS = {
    "heineken": 11, "amstel": 11, "brahma": 8,
    "agua garrafinha": 4, "agua 2l": 6, "guaravita": 2,
    "guaraviton": 6
}


def get_random_products_list(random_products_list_size: int, products_list_size: int):
    products_values = ["tapiocas", "hamburguers", "bebidas"]

    random_list = []
    for i in range(random_products_list_size):
        random_value = randint(0, 2)
        product = products_values[random_value]
        if product == "tapiocas":
            list_products = products_list(
                {"product": product, "values": TAPIOCAS}, products_list_size
            )

        elif product == "hamburguers":
            list_products = products_list(
                {"product": product, "values": HAMBURGUERES}, products_list_size
            )

        else:
            list_products = products_list(
                {"product": product, "values": BEBIDAS,}, products_list_size
            )
        
        if products_list_size == 1:
            list_products = list_products[0]
        random_list.append(list_products)

    return random_list

def products_list(products: dict[str, str], size: int):
    randomized_products = []
    products_values = products["values"]
    for i in range(size):
        random_product = randint(0, len(products_values) - 1)
        product = list(products_values.keys())[random_product]
        random_day = randint(0, 9)

        data = {
            "tipo_de_produto": products["product"],
            "produto": product,
            "valor": products_values[product],
            "data_da_venda": f"{20 + random_day}/06/2023"
            }

        randomized_products.append(data)
    return randomized_products

with open("./data.json", "w") as f:
    f.write(f"{json.dumps(get_random_products_list(200, 1))}")