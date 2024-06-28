from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form.get('num1'))
    num2 = float(request.form.get('num2'))
    operator = request.form.get('operator')

    if operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    elif operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Error: Invalid operator"

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)