# Image Segmentation using K-Nearest Neighbors (KNN) Algorithm

This project demonstrates image segmentation using the K-Nearest Neighbors (KNN) algorithm in Python. The project utilizes the OpenCV library for image processing tasks.

## Installation

To run this project, you need to have Python and OpenCV installed on your system. Follow the steps below to set up the project:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/ashkewww/Image-Segmentation-Using-KNN.git
   ```

2. Navigate to the project directory:

   ```
   cd Image-Segmentation-Using-KNN
   ```

3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the image segmentation script, follow these steps:

1. Run the python file app.py (Remember to install the requirements first)
2. In the webpage you'll see options to upload an image 
3. Add in the number of colors you want the image to be segmented in.
4. The Segmented Image will be displayed in the webpage itself

## Algorithm

The K-Nearest Neighbors (KNN) algorithm is a non-parametric classification algorithm. In image segmentation, KNN is used to classify each pixel into different classes based on the similarity of its neighboring pixels.

The algorithm works as follows:

1. Load the input image.

2. Convert the image to the desired color space (e.g., RGB, grayscale).

3. Preprocess the image if necessary (e.g., noise removal, smoothing).

4. For each pixel in the image, extract its neighboring pixels.

5. Calculate the similarity between the pixel and its neighbors using a distance metric (e.g., Euclidean distance).

6. Classify the pixel based on the majority class of its neighbors (using a voting mechanism).

7. Repeat steps 4-6 for all pixels in the image.

8. Save the segmented image.



## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


