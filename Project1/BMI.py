from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    BMI = None
    Category = ""
    try:
        if request.method == 'POST':
            height = int(request.form['height'])
            weight = int(request.form['weight'])

            BMI = round((weight * 10000) / (height * height), 2)
            if BMI < 18.5:
                Category = "Underweight"
            elif BMI < 24.9:
                Category = "Normal"
            elif BMI < 29.9:
                Category = "Overweight"
            else:
                Category = "Obese"
    except Exception as ex:
        print(ex)

    return render_template("BMI.html", BMI=BMI, Category=Category)


if __name__ == '__main__':
    app.run(debug=True)