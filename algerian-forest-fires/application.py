import pickle

from flask import Flask, render_template, request

# -------------------------
# Flask app setup
# -------------------------
application = Flask(__name__)
app = application  # useful for some deployments (WSGI servers)


# -------------------------
# Load ML model function
# -------------------------
def load_model():
    ridge_model = pickle.load(open("./models/ridge.pkl", "rb"))
    standard_scaler = pickle.load(open("./models/scaler.pkl", "rb"))
    return ridge_model, standard_scaler


# -------------------------
# Load model ONCE at startup
# -------------------------
ridge_model, standard_scaler = load_model()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_data():
    if request.method == "POST":
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws") or 0)
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))

        Classes = int(request.form.get("Classes"))
        Region = int(request.form.get("Region"))

        new_data = [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]

        new_data_scaled = standard_scaler.transform(new_data)

        prediction = ridge_model.predict(new_data_scaled)

        return render_template("home.html", results=prediction[0])
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
