from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary to store the latest sensor data
sensor_data = {}

@app.route('/')
def index():
    return render_template('index.html', data=sensor_data)

@app.route('/latest_data', methods=['GET'])
def latest_data():
    return jsonify(sensor_data)

@app.route('/data', methods=['POST'])
def update_data():
    global sensor_data
    sensor_data = request.json  # Update the global sensor_data with the incoming JSON
    print("Data received:", sensor_data)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)  # Make sure to use port 80 for public access
