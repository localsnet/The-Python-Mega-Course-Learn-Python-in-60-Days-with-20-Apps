from flask import Flask, render_template

#Website object
app = Flask(__name__)
#decorator
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/api/v1/<word>/")
def about(word):
    dictionary = {"definition": word.upper(), "word": word}
    return dictionary

if __name__ == "__main__":
    app.run(debug=True, port=5001)