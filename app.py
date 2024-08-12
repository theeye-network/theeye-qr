from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/<path:route>')
def render_certificate(route):
    image_path = f"/static/{route}.png"
    
    return render_template('certificate.html',user_image=image_path)

if __name__ == '__main__':
    app.run()