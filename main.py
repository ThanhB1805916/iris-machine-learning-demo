# Tham khảo tạo web: https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/


from flask import Flask, render_template, request

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

    return {
        "sep_len": sep_len,
        "sep_wid": sep_wid,
        "pet_len": pet_len,
        "pet_wid": pet_wid
    }


if __name__ == "__main__":
    app.run(debug=True)
