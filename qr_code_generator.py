import qrcode
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form['data']
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')
    qr_img.save('static/qr_code.png')
    return render_template('show_qr.html')

@app.route('/download_qr')
def download_qr():
    return send_file('static/qr_code.png', as_attachment=True)

if __name__ == '__main__':
    app.run()
