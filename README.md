# SCoralDet-Dataset 
> High-quality underwater coral detection dataset for machine learning and computer vision research.

[![Google Drive](https://img.shields.io/badge/Download-Google%20Drive-blue)](https://drive.google.com/file/d/1QIcbNdZ6HfU8E3VphbP7FmWtgXlxXV1W/view?usp=drive_link)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


---
## 🎥 Detection Video

![SCoralDet Detection Preview](https://github.com/RDXiaoLu/SCoralDet-Dataset/blob/main/Video/video.gif)

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
| Euphylliaancora | Platygyra | Sarcophyton |
|:---------------:|:---------:|:-----------:|
| ![Euphylliaancora](https://github.com/RDXiaoLu/SCoralDet-Dataset/blob/main/Data%20Preview/Euphylliaancora.png) | ![Platygyra](https://github.com/RDXiaoLu/SCoralDet-Dataset/blob/main/Data%20Preview/Platygyra.png) | ![Sarcophyton](https://github.com/RDXiaoLu/SCoralDet-Dataset/blob/main/Data%20Preview/Sarcophyton.png) |

| Wavinghand | Favosites | Sinularia |
|:----------:|:---------:|:---------:|
| ![Wavinghand](https://github.com/RDXiaoLu/SCoralDet-Dataset/blob/main/Data%20Preview/Wavinghand.png) | ![Favosites](https://github.com/RDXiaoLu/SCoralDet-Dataset/blob/main/Data%20Preview/Favosites.png) | ![Sinularia](https://github.com/RDXiaoLu/SCoralDet-Dataset/blob/main/Data%20Preview/Sinularia.png) |

---

## 🚀 Follow-Up Work: MambaCoral-DiffDet
Building upon the **SCoralDet** dataset, we developed **MambaCoral-DiffDet** as a refined and advanced framework for soft coral detection under complex underwater conditions. This work utilizes **diffusion models** to address data imbalance and improves detection accuracy using novel attention mechanisms and architecture modifications.

For more details, please refer to the [MambaCoral-DiffDet](https://github.com/RDXiaoLu/MambaCoral-DiffDet), where you can see how **SCoralDet** has been leveraged and extended in this project.

---


🎯 Applications
This dataset can be used for:

- Coral species classification
- Object detection tasks (e.g., YOLO, Faster R-CNN)
- Transfer learning on underwater datasets

---

## 🛠️ How to Use

### 1. **Download the Dataset**
To get started with the **SCoralDet Dataset**, you can download it directly from [Google Drive](https://drive.google.com/file/d/1QIcbNdZ6HfU8E3VphbP7FmWtgXlxXV1W/view?usp=drive_link).

### 2. **Preparing the Dataset**
Once you have the dataset, unzip the downloaded files. The dataset is organized into the following structure:

/home/featurize/data
├── annotations
└── image
    ├── Euphflfiaancora
    ├── Favosites
    ├── Platygyra
    ├── Sarcophyton
    ├── Sinularia
    └── WavingHand
    
/home/featurize/data ├── annotations # COCO format annotation files └── image # Images of coral species ├── Euphylliaancora # Images of Euphylliaancora species ├── Favosites # Images of Favosites species ├── Platygyra # Images of Platygyra species ├── Sarcophyton # Images of Sarcophyton species ├── Sinularia # Images of Sinularia species └── WavingHand # Images of WavingHand species

### 3. **Processing the Dataset**
You can use the **Dataset_process.ipynb** file to process the dataset and get the images in **PNG/JPEG** format with **COCO annotations**. You can split the dataset for training and validation.

### 4. **Converting COCO to YOLO Format**
If you'd like to use the dataset in **YOLO format**, use the **coco2yolo.py** script:

```bash
python coco2yolo.py --json_path your_coral_instances.json --save_path your_yolo_label_path

---

🔍 Citation & Preprint
For more details about our work, please refer to our preprint on SSRN:

**Lu, Zhaoxuan and Liao, Lyuchao and Xie, Xingang and Yuan, Hui.**  
**SCoralDet: Efficient Real-Time Underwater Soft Coral Detection with YOLO.**  
Available at SSRN: [https://ssrn.com/abstract=4992454](https://ssrn.com/abstract=4992454)  
or [http://dx.doi.org/10.2139/ssrn.4992454](http://dx.doi.org/10.2139/ssrn.4992454).

---

✨ Contributions
We welcome contributions to improve this dataset! Feel free to:

- Report issues or bugs.
- Submit pull requests for any enhancements.


