from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olááá! Minha aplicação Flask está rodando em Docker + NGINX!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# teste de git branch
