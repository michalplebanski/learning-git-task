shop_list = {
    "warzywaniak": ["buraki", "seler", "papryka"],
    "spoywczy": ["masło", "mleko", "chleb"]
}

print("Lista zakupów:\n")

for shop, product in shop_list.items():
    shopUpper = shop.capitalize()
    productUpper = [item.capitalize() for item in product]
    print(f"Idę do {shopUpper} kupić {productUpper}")

