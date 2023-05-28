from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/sobre")
def usuarios():
    return render_template("sobre.html")

@app.route("/reserva")
def reserva():
    return render_template("reserva.html")

if __name__ == "__main__":
    app.run(debug=True)

# servidor heroku
