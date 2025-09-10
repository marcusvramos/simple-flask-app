from flask import Flask, jsonify, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask OCI App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 40px;
            max-width: 600px;
            width: 90%;
        }
        h1 {
            color: #333;
            margin-bottom: 20px;
            text-align: center;
        }
        .info {
            background: #f7f7f7;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .info p {
            margin: 10px 0;
            color: #666;
        }
        .info strong {
            color: #333;
        }
        .status {
            display: inline-block;
            padding: 5px 10px;
            background: #10b981;
            color: white;
            border-radius: 5px;
            font-weight: bold;
        }
        .endpoints {
            margin-top: 30px;
        }
        .endpoints h2 {
            color: #333;
            margin-bottom: 15px;
        }
        .endpoint {
            background: #f0f0f0;
            padding: 10px 15px;
            border-radius: 5px;
            margin-bottom: 10px;
            font-family: monospace;
        }
        .endpoint a {
            color: #667eea;
            text-decoration: none;
        }
        .endpoint a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Flask OCI Application</h1>
        <div class="info">
            <p><strong>Status:</strong> <span class="status">Online</span></p>
            <p><strong>Servidor:</strong> {{ hostname }}</p>
            <p><strong>Data/Hora:</strong> {{ current_time }}</p>
            <p><strong>Versão:</strong> {{ version }}</p>
        </div>
        <div class="endpoints">
            <h2>Endpoints Disponíveis:</h2>
            <div class="endpoint">
                <a href="/">/</a> - Página inicial
            </div>
            <div class="endpoint">
                <a href="/api/health">/api/health</a> - Health check
            </div>
            <div class="endpoint">
                <a href="/api/info">/api/info</a> - Informações do sistema
            </div>
            <div class="endpoint">
                <a href="/api/status">/api/status</a> - Status da aplicação
            </div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, 
        hostname=os.uname().nodename,
        current_time=datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        version='1.0.0'
    )

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/info')
def info():
    return jsonify({
        'application': 'Flask OCI App',
        'version': '1.0.0',
        'hostname': os.uname().nodename,
        'platform': os.uname().sysname,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'running',
        'uptime': 'N/A',
        'memory': 'N/A',
        'cpu': 'N/A',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)