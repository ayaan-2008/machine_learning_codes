import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import cv2
import os
import pickle

from sklearn.cluster import KMeans

st.title("AI Drawing Pattern Analyzer")

canvas_result = st_canvas(
    fill_color="black",
    stroke_width=10,
    stroke_color="white",
    background_color="black",
    height=300,
    width=300,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:

    img = canvas_result.image_data

    gray = cv2.cvtColor(
        img.astype(np.uint8),
        cv2.COLOR_RGBA2GRAY
    )

    resized = cv2.resize(gray, (28, 28))

    normalized = resized / 255.0

    flattened = normalized.flatten()

    os.makedirs("drawings", exist_ok=True)

    sample_count = len(os.listdir("drawings"))

    np.save(
        f"drawings/sample_{sample_count}.npy",
        flattened
    )

    st.image(resized, caption="Processed Drawing")

    files = os.listdir("drawings")

    if len(files) >= 5:

        dataset = []

        for file in files:
            data = np.load(
                os.path.join("drawings", file)
            )
            dataset.append(data)

        dataset = np.array(dataset)

        kmeans = KMeans(
            n_clusters=3,
            random_state=42
        )

        labels = kmeans.fit_predict(dataset)

        current_cluster = labels[-1]

        st.success(
            f"Your drawing belongs to Cluster {current_cluster}"
        )

        st.write("Cluster assignments:")
        st.write(labels)