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
- Pothole_Detection.ipynb - Jupyter notebook containing project code and visualizations
