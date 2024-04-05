from flask import Flask, render_template, request
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

pings = [{'resposta': 'Olá, mundo!', 'time': '05/04/2024 15:45:51'}]

# Rota para o htmx de ping
@app.route('/ping')
def index():
    mensagem = str(request.form.get("mensagem"))
    pings.append({'resposta': mensagem, 'data-e-hora': time.strftime("%d/%m/%Y %H:%M:%S")})
    print(pings)
    return render_template('ping.html')

# Rota para o htmx de pong
@app.route('/pong')
def pong():
    print(pings)
    return render_template('pong.html', pings=pings)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)