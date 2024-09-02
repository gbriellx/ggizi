from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    rate = data['rates']['BRL']
    
    result = amount * rate
    return jsonify({'result': f'{result:.2f}', 'rate': f'{rate:.4f}'})

from app import app

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)

