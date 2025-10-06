from flask import Flask, render_template, send_file
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return render_template('index.html', hostname=hostname)

@app.route('/about')
def about():
    return '''
    <h1>About This Server</h1>
    <p>This is a Raspberry Pi 5 running Flask!</p>
    <p><a href="/">Back to Home</a></p>
    '''

@app.route('/download')
def download_file():
    return send_file('static/raspberry_pi.png', 
                     as_attachment=True,
                     download_name='raspberry_pi_image.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
