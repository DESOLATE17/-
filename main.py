from flask import Flask
from generator import prime_generator

app = Flask(__name__)


@app.route('/')
def index():
    return ""


@app.route('/<int:n>')
def count_number(n):
    return str(list(prime_generator(n)))


if __name__ == "__main__":
    app.run(debug=True)