# SCoralDet: Efficient real-time underwater soft coral detection with YOLO  &  SCoralDet Dataset
> Efficient methods for underwater coral detection and high-quality underwater coral detection dataset for machine learning and computer vision research.

[![Google Drive](https://img.shields.io/badge/Download-Google%20Drive-blue)](https://drive.google.com/file/d/1QIcbNdZ6HfU8E3VphbP7FmWtgXlxXV1W/view?usp=drive_link)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![SCoralDet Dataset SOTA](https://img.shields.io/badge/SCoralDet%20Dataset-SOTA-blue)](https://paperswithcode.com/dataset/scoraldet-dataset-1)  

---
## 🎥 Detection Video

![SCoralDet Detection Preview](https://github.com/RDXiaoLu/SCoralDet-Dataset/blob/main/Video/video.gif)

---

## 📅 Recent Updates  
- **[2024/12/22]**: Added **detailed instructions** for integrating and using SCoralDet source code within the Ultralytics YOLO framework. 🎉
- **[2024/12/18]**: We have uploaded the **core improvement source code of SCoralDet**! 😊  
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
We also provide **coral videos** as part of the dataset. You can access and download them via the following Google Drive link: [Google Drive - Coral Videos (https://drive.google.com/file/d/1gGZgNfaqIUClyeygsUnVDogAIwkJLGx9/view?usp=drive_link)  

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

## 🛠️ How to Use Dataset

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

## 📂 SCoralDet Project Structure  

```markdown 
|-- SCoralDet/  
    |-- README.md                  # Documentation for the project 
    |-- lib/                       # Core library containing configurations, modules, and utilities
        |-- cfg/
            |-- models/
                |-- v10/           # YOLOv10 model configurations
                    |-- yolov10n.yaml             # Main YOLOv10n model structure                 
                    |-- yolov10n_backbone.yaml    # Main YOLOv10n MPFB-backbone configuration     
                    |-- yolov10n_lightneck.yaml   # YOLOv10n lightweight neck configuration
        |-- nn/       
            |-- extra_modules/     # Additional model modules       
                |-- block.py       # Includes custom modules: MPFB & LightNeck  
        |-- utils/
            |-- tal.py             # Implements APT  
         
```
    
---

## ⚙️ How to Use the Source Code

### 1. **Environment Setup**
Follow the [Ultralytics YOLO Framework v8.3.51](https://github.com/ultralytics/ultralytics/tree/v8.3.51) guide to set up the environment and dependencies.
Install PyTorch:
```markdown
pip install torch==2.2.0 torchvision==0.17.2 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu121
```
### 2. **Integrate SCoralDet into Ultralytics YOLO Framework**
After setting up Ultralytics YOLO, the next step is to add SCoralDet's custom code to the framework. Below are the specific modules and their purposes:
```markdown
1. Add the `extra_modules/` folder:  
   └── Copy the `block.py` file into the framework's directory for module extensions.  
       - Purpose: Implements MPFB (Multi-Path Fusion Block) and LightNeck modules.
2. Add the `utils/tal.py` file:  
   └── Copy this utility script into the framework.  
       - Purpose: Provides the APT algorithm.
3. Copy the following configuration files from lib/cfg/models/v10/ into the YOLO framework:
    - `yolov10n_backbone.yaml`: Configures the MPFB backbone module.  
    - `yolov10n_lightneck.yaml`: Defines the lightweight neck structure.  
```
### 3. **Training the Model**
Once SCoralDet is integrated, you can begin training the model by executing the following command:
```markdown
python train.py
```
### 4. **Model Validation**
After training, validate the model’s performance using the following command:
```markdown
python val.py
```

---

## 🔍 Citation  
If you find our work useful, please consider citing us or giving us a star ⭐. 

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

## ✨ Contributions & 📬 Contact Us
We welcome contributions to improve this dataset and code! Feel free to:

- Report issues or bugs.
- Submit pull requests for any enhancements.
- Email us directly at [luzhaoxuan@smail.fjut.edu.cn]. 

