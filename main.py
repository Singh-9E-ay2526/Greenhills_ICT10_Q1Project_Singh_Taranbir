from pyscript import document


def create_order(event):
    subtotal = 0

    items = document.querySelectorAll("input[type='checkbox']")

    for item in items:
        if item.checked:
            subtotal = subtotal + float(item.value)

    vat = subtotal * 0.12
    total = subtotal + vat

    document.querySelector("#subtotal").textContent = f"{subtotal:.2f}"
    document.querySelector("#vat").textContent = f"{vat:.2f}"
    document.querySelector("#total").textContent = f"{total:.2f}"

    document.querySelector("#receipt").style.display = "block"
    def generate_sku(event):
    category = document.querySelector("#category").value
    product_name = document.querySelector("#product-name").value
    quantity = document.querySelector("#quantity").value

    sku = category + "-" + product_name + "-" + quantity

    document.querySelector("#sku").textContent = sku