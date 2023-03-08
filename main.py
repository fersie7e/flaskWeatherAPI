import flask
import pandas as pd

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperatura": temperature}


if __name__ == "__main__":
    app.run(debug=True)