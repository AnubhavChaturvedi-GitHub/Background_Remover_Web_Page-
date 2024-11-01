from flask import Flask, request, render_template, send_file
from rembg import remove
from PIL import Image
import io
import os
app = Flask(__name__, template_folder='Template')  # Specify the template folder
@app.route('/')
def home():
    return render_template('index.html')  # Load the main page
@app.route('/remove_background', methods=['POST'])
def remove_background():
    if 'file' not in request.files:
        return "No file provided", 400
    file = request.files['file']
    img = Image.open(file.stream)
    # Remove background
    output = remove(img)
    # Save the output image to a byte stream
    img_io = io.BytesIO()
    output.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')
if __name__ == '__main__':
    app.run(debug=True)
