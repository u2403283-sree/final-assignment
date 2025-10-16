from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        height = float(request.form['height']) / 100
        weight = float(request.form['weight'])
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
            
        return render_template('index.html', bmi=round(bmi, 2), category=category)
        
    except Exception as e:
        return render_template('index.html', error="Please enter valid numbers!")

if __name__ == '__main__':
    app.run(debug=True)