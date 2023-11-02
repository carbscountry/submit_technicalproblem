import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
# Set up the logging
logging.basicConfig(filename='/var/log/myapp/app.log', level=logging.INFO)

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@app.route('/fib', methods=['GET'])
def get_fibonacci():
    try:
        n = int(request.args.get('n'))
        if n <= 0:
            raise ValueError
        result = fibonacci(n)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"status": 400, "message": "Bad request."}), 400

if __name__ == "__main__":
    app.run(debug=True)
