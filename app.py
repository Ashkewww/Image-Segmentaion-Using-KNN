from flask import Flask, render_template, redirect, url_for, request
from scripts.Segmentation import segmentImages
import cv2
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        image = request.files['image']
        k = int(request.form['number'])
        image_path = '''static/temp.jpg'''
        image.save(image_path)
        segmentImages(image_path, k)
        filter_image_path = '''static/segmented.jpg'''

        return render_template('home.html', image_path=filter_image_path)
    return render_template('home.html')
if __name__ == '__main__':
    app.run()