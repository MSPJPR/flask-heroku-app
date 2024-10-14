from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageEnhance, ImageFilter
import os

app = Flask(__name__)

# Ensure the 'static' folder exists for storing processed images
if not os.path.exists('static'):
    os.makedirs('static')

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for processing the image
@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return redirect(request.url)

    image_file = request.files['image']
    if image_file.filename == '':
        return redirect(request.url)

    # Open the image
    img = Image.open(image_file)

    # Get the selected filter from the form
    filter_option = request.form.get('filter')

    # Apply the selected filter
    if filter_option == 'brightness':
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.5)
    elif filter_option == 'contrast':                                           enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.5)
    elif filter_option == 'grayscale':
        img = img.convert('L')
    elif filter_option == 'sharpen':
        img = img.filter(ImageFilter.SHARPEN)
    elif filter_option == 'smooth':
        img = img.filter(ImageFilter.SMOOTH)
    elif filter_option == 'compress':
        img = img.convert('RGB')

    # Save the processed image in the 'static' directory
    processed_image_path = os.path.join('static', 'processed_image.jpg')
    img.save(processed_image_path)

    # Pass the path to the processed image to the template
    return render_template('index.html', processed_image='processed_ima>

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
