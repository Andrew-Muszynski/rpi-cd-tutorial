from flask import Flask, render_template, send_file, jsonify
import socket
from sensor import get_sensor_data  # Import your sensor module

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    sensor_data = get_sensor_data()
    return render_template('index.html', 
                         hostname=hostname,
                         sensor_data=sensor_data)

@app.route('/api/sensor')
def sensor_api():
    """JSON endpoint for sensor data - useful for checking values"""
    return jsonify(get_sensor_data())

@app.route('/about')
def about():
    return '''
    <h1>About This Server</h1>
    <p>This is a Raspberry Pi 5 running Flask with sensor integration!</p>
    <p><a href="/">Back to Home</a></p>
    '''

@app.route('/download')
def download_file():
    return send_file('static/raspberry_pi.png', 
                     as_attachment=True,
                     download_name='raspberry_pi_image.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
