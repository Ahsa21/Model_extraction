from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/api/welcome', methods=['GET'])
def welcome():
    name = request.args.get('name', 'World')
    return jsonify(message=f'Hello, {name}!')


if __name__ == '__main__':
    app.run(debug=True)