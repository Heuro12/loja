from flask import Flask, render_template
import requests

app = Flask(__name__)

# URL da API do painel (troque pelo link final do seu painel)
API_URL = "https://painel-ly5m.onrender.com/api/produtos"

@app.route("/")
def index():
    try:
        response = requests.get(API_URL)
        produtos = response.json()
    except Exception as e:
        print("Erro ao conectar API:", e)
        produtos = []
    return render_template("index.html", produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
