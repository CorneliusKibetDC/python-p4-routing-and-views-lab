#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route (Updated to return plain text)
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to console
    return parameter  # Return plain text instead of HTML tags

# Count route (Updated to use newline characters instead of <br>)
@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n'  # Ensure the last number is followed by a newline

# Math route (Updated to return only the result value without HTML)
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return '<p>Error: Division by zero is not allowed.</p>'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return '<p>Error: Unsupported operation.</p>'
    
    return str(result)  # Return just the result as a string, no HTML tags

if __name__ == '__main__':
    app.run(port=5555, debug=True)
