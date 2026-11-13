from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUEST_COUNT = Counter('app_requests_total', 'Total de peticiones a la aplicacion')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return "¡Hola! Mi taller de observabilidad con Flask está activo"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)