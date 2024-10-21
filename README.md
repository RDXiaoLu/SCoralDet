# SCoralDet-Dataset 🪸

[![Google Drive](https://img.shields.io/badge/Download-Google%20Drive-blue)](https://drive.google.com/file/d/1QIcbNdZ6HfU8E3VphbP7FmWtgXlxXV1W/view?usp=drive_link)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📝 Overview
The **SCoralDet Dataset** is a high-quality underwater coral dataset, containing **646** annotated images collected from the **Coral Germplasm Conservation and Breeding Center** at **Hainan Tropical Ocean University** in Sanya, China. This dataset is specifically designed for coral detection and recognition tasks, making it ideal for researchers and practitioners working on **underwater image analysis**, **marine biology**, and **computer vision applications**.

### 🌊 Coral Species:
The dataset includes images from the following **six coral species**:
- **Euphylliaancora**
- **Favosites**
- **Platygyra**
- **Sarcophyton**
- **Sinularia**
- **Wavinghand**

### 📂 Dataset Details:
- **Total images**: 646
- **Format**: PNG/JPEG
- **Annotations**: Bounding boxes in COCO format
- **Resolution**: Variable (high-resolution images)

---

## 📥 Download
You can download the dataset from [Google Drive](https://drive.google.com/file/d/1QIcbNdZ6HfU8E3VphbP7FmWtgXlxXV1W/view?usp=drive_link).

---

## 🐚 Dataset Preview
Here are a few samples from the dataset:

![Euphylliaancora Coral](path-to-sample-image1.jpg)
![Favosites Coral](path-to-sample-image2.jpg)

---

## 🧪 How to Use
To get started with the **SCoralDet Dataset**, follow these steps:
1. **Download the dataset** using the link above.
2. Extract the files to your local machine.
3. Load the dataset into your machine learning model using your preferred data loading library (e.g., `torchvision.datasets`, `tf.data`).

```python
# Example: Load dataset in PyTorch
from torchvision import datasets

dataset = datasets.ImageFolder(root='path_to_dataset')
