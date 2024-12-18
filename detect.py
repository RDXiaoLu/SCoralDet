import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
from ultralytics import RTDETR


# 推理参数官方详解链接：https://docs.ultralytics.com/modes/predict/#inference-sources:~:text=of%20Results%20objects-,Inference%20Arguments,-model.predict()

if __name__ == '__main__':
    model = YOLO('/mnt/hdd/yuanhui/ultralytics-main/ultralytics/results/UTDAC_YOLOv8/weights/best.pt') # select your model.pt path
    model.predict(source='/mnt/hdd/yuanhui/ultralytics-main/dataset/UTDAC_show',
                  imgsz=640,
                  project='runs/UTDAC_show',
                  name='SCoralDet',
                  save=True,
                  # conf=0.2,
                  # iou=0.7,
                  # agnostic_nms=True,
                  # visualize=True, # visualize model features maps
                  # line_width=2, # line width of the bounding boxes
                  # show_conf=False, # do not show prediction confidence
                  # show_labels=False, # do not show prediction labels
                  # save_txt=True, # save results as .txt file
                  # save_crop=True, # save cropped images with results
                )
    
    
# Validating /mnt/hdd/yuanhui/ultralytics-main/ultralytics/results/UTDAC_YOLOv8/weights/best.pt...
# Ultralytics YOLOv8.2.50 🚀 Python-3.9.18 torch-2.1.1+cu118 CUDA:0 (Tesla V100-SXM2-32GB-LS, 32501MiB)
# YOLOv8 summary (fused): 168 layers, 3006428 parameters, 0 gradients, 8.1 GFLOPs
#                  Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 21/21 [00:09<00:00,  2.33it/s]
#                    all       1292       9478      0.825      0.761      0.838      0.501
#                echinus        978       4730      0.863      0.834      0.897      0.524
#            holothurian        555       1338      0.758      0.646      0.727      0.398
#                scallop        289       1617      0.829      0.756      0.845      0.533
#               starfish        635       1793      0.849      0.807      0.883       0.55
# Speed: 0.2ms preprocess, 0.9ms inference, 0.0ms loss, 1.2ms postprocess per image
# Results saved to /mnt/hdd/yuanhui/ultralytics-main/ultralytics/results/UTDAC_YOLOv8
# MLflow: results logged to runs/mlflow
# MLflow: disable with 'yolo settings mlflow=False'