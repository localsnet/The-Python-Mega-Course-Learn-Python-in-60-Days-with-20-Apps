from flask import Flask, render_template
import pandas

#Website object
app = Flask(__name__)
#decorator
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pandas.read_csv("")
    temperature = df.station(date)

if __name__ == "__main__":
    app.run(debug=True)