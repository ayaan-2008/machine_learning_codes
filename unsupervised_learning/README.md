<div align="center">

# Shape Analyzer

### An Interactive Drawing Pattern Analyzer Using Unsupervised Learning

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)

[View Code](unsupervised_learning.py) | [Back to Index](../README.md)

</div>

---

## Overview

**AI Drawing Pattern Analyzer** is an interactive Machine Learning project that demonstrates the fundamentals of **Unsupervised Learning**. Users can draw shapes on a digital canvas, and the system automatically groups similar drawings into clusters using the K-Means algorithm.

Unlike supervised learning models, this system does **not** receive labels such as "Circle," "Square," or "Triangle." Instead, it analyzes characteristics and discovers patterns on its own.

---

## Features

- Interactive drawing canvas
- Real-time image preprocessing
- Automatic feature extraction
- K-Means clustering
- Unsupervised pattern discovery
- Live cluster assignment for user drawings

---

## Demo

<!-- Add your screenshot/demo here -->
<!-- ![Shape Analyzer Demo](path/to/demo.png) -->

> Screenshot coming soon!

<!-- Add demo video here -->
<!-- https://www.youtube.com/watch?v=YOUR_VIDEO_ID -->

> Demo video coming soon!

---

## How It Works

1. User draws a shape on the canvas
2. Drawing is converted to grayscale image
3. Image is resized and transformed into numerical features
4. Features are stored as part of a growing dataset
5. K-Means clustering groups similar drawings together
6. Application displays the cluster assigned to the latest drawing

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Interactive web application |
| OpenCV | Image processing |
| NumPy | Numerical operations |
| Scikit-learn | K-Means clustering |
| Pillow | Image handling |

---

## Project Structure

```
unsupervised_learning/
├── README.md                     # This file
├── unsupervised_learning.py      # Main code
├── drawings/                     # Sample drawing data
│   ├── sample_0.npy
│   ├── sample_1.npy
│   └── ... (188+ samples)
└── requirements.txt              # Dependencies
```

---

## Installation & Usage

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Steps

```bash
# Clone the repository
git clone https://github.com/ayaan-2008/machine_learning_codes.git

# Navigate to project folder
cd machine_learning_codes/unsupervised_learning

# Install dependencies
pip install -r requirements.txt

# Run the project
streamlit run unsupervised_learning.py
```

### Alternative Run Method

```bash
python -m streamlit run unsupervised_learning.py
```

---

## ML Concepts

| Concept | Application |
|---------|-------------|
| Unsupervised Learning | No predefined labels |
| K-Means Clustering | Grouping similar shapes |
| Feature Extraction | Converting drawings to numerical data |
| Pattern Recognition | Identifying shape similarities |
| Image Processing | Preprocessing user drawings |
| Data Preparing | Normalizing and resizing images |

---

## Future Enhancements

- PCA-based visualization of clusters
- Autoencoder-based feature extraction
- Improved shape recognition accuracy
- Additional clustering algorithms (DBSCAN, Hierarchical)
- Enhanced user interface and analytics dashboard
- Export cluster results

---

## Author

**Mohammed Abdul Ayaan**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/ayaan-2008)

---

<div align="center">

[Back to Main Index](../README.md)

</div>
