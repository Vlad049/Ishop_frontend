from flask import Flask, flash, render_template, redirect, url_for

from src.data import data_actions


app = Flask(__name__, template_folder="src/templates")
app.secret_key = "abc"


@app.get("/")
def index():
    products = data_actions.get_products()
    return render_template("index.html", products=products)


@app.get("/products/<product_id>/")
def get_product(product_id):
    product = data_actions.get_product(product_id)
    return render_template("product.html", product=product)


@app.get("/buy_products/<product_id>/")
def buy_product(product_id):
    product = data_actions.get_product(product_id)
    flash(f"Вітаємо з покупкою '{product['name']}'")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
