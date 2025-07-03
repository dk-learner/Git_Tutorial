from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load model and known fruit names
model = pickle.load(open("model.pkl", "rb"))
known_fruits = pickle.load(open("known_fruits.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        fruit_name = request.form["fruit"].strip().lower()
        if fruit_name not in known_fruits:
            prediction = "None"
        else:
            prediction = model.predict([fruit_name])[0]
    return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    # Bind to PORT provided by Render/Heroku
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=False, host='0.0.0.0', port=port)
