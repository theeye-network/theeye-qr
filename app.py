from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:route>')
def render_certificate(route):
    image_path = f"/static/{route}.png"
    
    return render_template('certificate.html',user_image=image_path)

def main():
    app.run(host='0.0.0.0',
        port=9327,
        debug=True)

if __name__ == '__main__':
    app.run()
