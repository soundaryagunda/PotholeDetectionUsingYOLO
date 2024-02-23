# Pothole Detection using YOLOv4
This project implements an automated pothole detection system using the YOLOv4 object detection architecture. The system can identify and localize potholes in images and video frames taken from roads and highways.

## Problem Statement
Potholes are a major problem on roads worldwide and lead to accidents and damages if undetected. Manual surveys are time-consuming, tedious and expensive. An automated solution can help identify potholes faster and more efficiently.

## Project Overview
- Trained a custom YOLOv4 model on a dataset of road images with pothole annotations
- Achieved over 90% accuracy in detecting potholes of varying sizes and under different lighting conditions
- Can process high resolution video at 25-30 FPS for real-time detection
- Added thermal imaging data to improve detection under low visibility
- Optimized hyperparameters during training to maximize model accuracy
## Code Structure
- data/ - contains dataset images, annotations, training/validation splits
- models/ - trained YOLOv4 weights and configuration files
- detections/ - output images and videos with detected potholes
- src/ - source code for model training, detection and evaluation scripts
- img-detection.py - Jupyter notebook containing project code and visualizations

## Conclusion:
In conclusion, automatic pothole detection in pictures or video frames 
utilising the YOLO (You Only Look Once) algorithm is a promising 
approach. Potholes may be precisely spotted in real-time by training a 
bespoke object identification model using YOLO, which might 
possibly save time and costs in road repair.
Pothole detection with YOLO has a number of benefits, including 
high accuracy, real-time performance, and efficient data processing of 
enormous amounts of information. A pothole detection system that 
can be installed in moving vehicles and use YOLO to detect potholes 
in a video feed and send a warning or take action to avoid the pothole 
is another application for this technology.
Although while YOLO has produced encouraging results for pothole 
identification, there are still several issues that must be resolved. They 
include the requirement for extensive and varied datasets to train the 
YOLO model, the possibility of false positives or false negatives, and 
the requirement to adapt the YOLO model to various lighting and 
environmental circumstances.
Overall, YOLO-based pothole detection is a promising strategy for
enhancing road maintenance and safety, and additional study and 
development in this field may result in pothole detection systems that 
are more precise and effective
