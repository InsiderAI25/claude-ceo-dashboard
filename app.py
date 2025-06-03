from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "status": "Claude CEO Dashboard is online.",
        "offers": [
            {"partner": "DraftKings", "status": "Approved"},
            {"partner": "PrizePicks", "status": "Flagged"},
            {"partner": "SharpBoost", "status": "Greenlight"}
        ],
        "logs": [
            "DROPZONE_CLEANUP_001 complete",
            "Vault log: SENTINEL_SECURE_002 sealed"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
