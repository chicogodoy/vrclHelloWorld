from flask import Flask, render_template

app = Flask(__name__)

def get_data():
    return {
        "titulo": "Meu Resultado",
        "mensagem": "Olá, mundo!",
        "data": "29 de abril de 2026",
        "itens": ["Item 1", "Item 2", "Item 3"]
    }

@app.route("/")
def index():
    dados = get_data()
    return render_template("index.html", **dados)

if __name__ == "__main__":
    app.run(debug=True, extra_files=['templates/index.html'])