# SCoralDet: Efficient real-time underwater soft coral detection with YOLO  & SCoralDet Dataset
> High-quality underwater coral detection dataset for machine learning and computer vision research.

[![Google Drive](https://img.shields.io/badge/Download-Google%20Drive-blue)](https://drive.google.com/file/d/1QIcbNdZ6HfU8E3VphbP7FmWtgXlxXV1W/view?usp=drive_link)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![SCoralDet Dataset SOTA](https://img.shields.io/badge/SCoralDet%20Dataset-SOTA-blue)](https://paperswithcode.com/dataset/scoraldet-dataset-1)  

---
## 🎥 Detection Video

![SCoralDet Detection Preview](https://github.com/RDXiaoLu/SCoralDet-Dataset/blob/main/Video/video.gif)

---

## 📅 Recent Updates  
- **[2024/12/16]**: We are maintaining the **SCoralDet Dataset** on [Papers with Code](https://paperswithcode.com/dataset/scoraldet-dataset-1).  
- **[2024/12/13]**: Our paper **SCoralDet: Efficient real-time underwater soft coral detection with YOLO** has recently been published! [[Paper]](https://www.sciencedirect.com/science/article/pii/S1574954124004795)
- **[2024/12/01]**: We’ve added specific instructions on how to use the dataset for your research!
- **[2024/11/20]**: We've opened up our dataset! [[SCoralDet-Dataset]](https://drive.google.com/file/d/1QIcbNdZ6HfU8E3VphbP7FmWtgXlxXV1W/view?usp=drive_link)
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


## 🎯 Applications
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

```markdown 
/your_dataset_path
├── annotations
└── image
    ├── Euphflfiaancora
    ├── Favosites
    ├── Platygyra
    ├── Sarcophyton
    ├── Sinularia
    └── WavingHand
```
   
- **`annotations/`**: Contains annotation files in **COCO format** for each image in the `image/` directory.
- **`image/`**: Contains images for each of the six coral species, organized in separate subdirectories.

### 3. **Processing the Dataset**
You can use the **Dataset_process.ipynb** file to process the dataset and get the images in **PNG/JPEG** format with **COCO annotations**. You can split the dataset for training and validation.

### 4. **Converting COCO to YOLO Format**
If you'd like to use the dataset in **YOLO format**, use the **coco2yolo.py** script:

```bash
python coco2yolo.py --json_path your_coral_instances.json --save_path your_yolo_label_path
```

---


## 🔍 Citation 
For more details about our work, please refer to our paper:

```markdown 
@ARTICLE{lu2024scoraldet,  
         author={Lu, Zhaoxuan and Liao, Lyuchao and Xie, Xingang and Yuan, Hui},  
         title={SCoralDet: Efficient real-time underwater soft coral detection with YOLO},  
         journal={Ecological Informatics},  
         year={2024},  
         artnum={102937},  
         issn={1574-9541},  
         doi={10.1016/j.ecoinf.2024.102937},  
}  
```

---

## ✨ Contributions
We welcome contributions to improve this dataset! Feel free to:

- Report issues or bugs.
- Submit pull requests for any enhancements.


