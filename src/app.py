from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "devops-project-app"}), 200

@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from DevOps Project!"}), 200

@app.route('/api/v1/version', methods=['GET'])
def version():
    return jsonify({"version": "1.0.0"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
