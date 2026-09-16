from pyscript import document


def create_order(event):

    subtotal = 0

    americano = document.getElementById("americano")
    spanish_latte = document.getElementById("spanish-latte")
    cold_brew = document.getElementById("cold-brew")
    affogato = document.getElementById("affogato")
    caramel_macchiato = document.getElementById("caramel-macchiato")

    if americano.checked:
        subtotal = subtotal + float(americano.value)

    if spanish_latte.checked:
        subtotal = subtotal + float(spanish_latte.value)

    if cold_brew.checked:
        subtotal = subtotal + float(cold_brew.value)

    if affogato.checked:
        subtotal = subtotal + float(affogato.value)

    if caramel_macchiato.checked:
        subtotal = subtotal + float(caramel_macchiato.value)

    vat = subtotal * 0.12
    total = subtotal + vat

    document.getElementById("subtotal").textContent = subtotal
    document.getElementById("vat").textContent = vat
    document.getElementById("total").textContent = total


def generate_sku(event):

    category = document.getElementById("category").value
    product_name = document.getElementById("product-name").value
    quantity = document.getElementById("quantity").value

    sku = category + "-" + product_name + "-" + quantity

    document.getElementById("sku").textContent = sku
