# Industrial Safety Gear Detection using YOLOv8 on a Custom Dataset

## Overview
This project focuses on detecting industrial safety gear using a custom object detection model. The model was fine-tuned on a self-annotated dataset with specific safety gear classes. The annotations were created using LabelImg, and the model was trained using YOLOv8. The final model is capable of performing real-time detection via a webcam and processing video input using OpenCV.

## Project Structure
- `data/`: Contains the custom dataset and annotations.
- `models/`: Directory to save the trained YOLOv8 model.
- `output/`: Contains the annotated sample output files
- `training/detect/`: Contains the model trained data and affiliated results.

## Features
- **Custom Object Detection:** Developed a model for detecting industrial safety gear using a self-annotated dataset.
- **Real-time Detection:** Integrated webcam-based real-time object detection.
- **Video Processing:** Used OpenCV for object detection in video files.
- **Transfer Learning:** Leveraged YOLOv8 for fine-tuning on the custom dataset.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/industrial-safety-gear-detection.git

2. Install the required dependencies : 
   ```bash
   pip install -r requirements.txt

3. Open and run app.py file : 
   ```bash
   python main.py

## Dataset
The custom dataset was annotated using [LabelImg](https://github.com/HumanSignal/labelImg). It includes images of various industrial environments with annotated safety gear such as helmets, gloves, goggles and jacket.

## Demo
https://github.com/user-attachments/assets/08a9e98b-72f1-4745-803d-40c16656e17d

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the [MIT License](LICENSE).
