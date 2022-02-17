from os import sep
from flask import Flask, render_template, request
from iris_prediction import tree_predict
app = Flask(__name__)


# Hiển thị trang để nhập thông tin
@app.route("/")
def home():
    return render_template("index.html")

# Xử lý submit form


@app.route('/predict', methods=['POST'])
def predict_data():
    # Get form data
    sep_len = request.form['sep_len']
    sep_wid = request.form['sep_wid']

    pet_len = request.form['pet_len']
    pet_wid = request.form['pet_wid']

    # Convert to number
    sep_len = float(sep_len)
    sep_wid = float(sep_wid)
    pet_len = float(pet_len)
    pet_wid = float(pet_wid)

    data = [sep_len, sep_wid, pet_len, pet_wid]

    # Predict
    result = tree_predict(data)

    # Return result
    return render_template("result.html", params={"data": data, "result": result})


if __name__ == "__main__":
    app.run(debug=True)
