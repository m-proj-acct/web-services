# app.py (Python Service)
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Endpoint to call the Go service
@app.route('/tow', methods=['GET'])
def call_go_service():
    vehicle_number = request.args.get('vehicle')
    if not vehicle_number:
        return jsonify({"error": "Vehicle number is required"}), 400

    # Call the Go service using Render's internal DNS
    go_service_url = f"https://go-services-t8lc.onrender.com/assist?vehicle={vehicle_number}"
    try:
        response = requests.get(go_service_url)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Go service error", "details": response.text}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to contact Go service", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

