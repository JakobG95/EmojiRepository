from flask import Flask

app = Flask(__name__)

def BuchstabenAnzahl(word): 
    return f"Die Anzahl der Buchstaben in '{word}' beträgt: {len(word)}"

@app.route('/')
def index():
    output1 = BuchstabenAnzahl("Penis")
    output2 = BuchstabenAnzahl("BVB gewinnt2")
    return f"<h1>{output1}</h1><h1>{output2}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
