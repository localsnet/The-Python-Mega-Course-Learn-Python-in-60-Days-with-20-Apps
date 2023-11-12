from flask import Flask, render_template
import pandas as pd

#Website object
app = Flask(__name__)

df = pd.read_csv("dictionary.csv")
#decorator
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/api/v1/<word>/")
def about(word):
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    print(type(definition))
    print(definition)
    dictionary = {"definition": definition, "word": word}
    return dictionary

if __name__ == "__main__":
    app.run(debug=True, port=5001)