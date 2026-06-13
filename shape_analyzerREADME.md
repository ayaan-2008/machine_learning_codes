# AI Drawing Pattern Analyzer

## Overview

AI Drawing Pattern Analyzer is an interactive Machine Learning project that demonstrates the fundamentals of **Unsupervised Learning**. The application allows users to draw shapes on a digital canvas and automatically groups similar drawings into clusters using the K-Means clustering algorithm.

Unlike supervised learning models, this system does not receive labels such as "Circle," "Square," or "Triangle." Instead, it analyzes the characteristics of each drawing and discovers patterns on its own.

## Features

* Interactive drawing canvas
* Real-time image preprocessing
* Automatic feature extraction
* K-Means clustering
* Unsupervised pattern discovery
* Live cluster assignment for user drawings

## How It Works

1. The user draws a shape on the canvas.
2. The drawing is converted into a grayscale image.
3. The image is resized and transformed into numerical features.
4. Features are stored as part of a growing dataset.
5. K-Means clustering groups similar drawings together.
6. The application displays the cluster assigned to the latest drawing.

## Machine Learning Concepts

* Unsupervised Learning
* K-Means Clustering
* Feature Extraction
* Pattern Recognition
* Image Processing
* Data Preprocessing

## Technologies Used

* Python
* Streamlit
* OpenCV
* NumPy
* Scikit-learn
* Pillow

## Installation

Install the required packages:

```bash
pip install streamlit
pip install streamlit-drawable-canvas
pip install numpy
pip install opencv-python
pip install pillow
pip install scikit-learn
```

## Running the Project

```bash
streamlit run unsupervised_learning.py
```

or

```bash
python -m streamlit run unsupervised_learning.py
```

## Project Objective

The goal of this project is to demonstrate how unsupervised machine learning algorithms can identify hidden patterns and similarities within data without relying on predefined labels. It serves as a practical introduction to clustering techniques and interactive machine learning applications.

## Future Enhancements

* PCA-based visualization of clusters
* Autoencoder-based feature extraction
* Improved shape recognition accuracy
* Additional clustering algorithms such as DBSCAN
* Enhanced user interface and analytics dashboard

## Author

Abdul Ayaan
