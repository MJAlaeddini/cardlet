from flask import Flask, render_template
from card import Card

app = Flask(__name__)

#tento seznam karet se musí načítat z cookies
cardset = []

@app.route("/")
@app.route("/cardlet", methods=["GET"])
def cardlet():
    return render_template("cardlet.html")

@app.route("/cards", methods=["GET", "POST"])
def cards():
    return render_template("cards.html", cardset=cardset)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")

#co potřebujeme
#1. Možnost si vytvořit kartu
#2. Zobrazit vytvořené karty v náhledu
#3. Zobrazit vytvořené karty na fullscreenu
#4. Otáčet karty
#5. Exportovat sadu karet do zip s jpg
#6. Exportovat sadu karet do pdf
#7. Pamatovat si uložené karty z cookie
#8. Provést jednotkové testy na karty
#9. Provést penetrační testy nad aplikací

#proces