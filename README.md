# Labelme Improved

This is an improved version of the [LabelMe](https://github.com/wkentaro/labelme) software. I have made several improvements to the original functionality, focusing on optimizing the annotation process, label copying, and keyboard shortcuts to make annotation tasks faster and more efficient.

## Improvements

1. **Optimized Annotation Process**  
   The annotation workflow has been redesigned to reduce unnecessary steps, significantly decreasing the annotation time. This allows users to complete annotation tasks more quickly.

2. **Enhanced Label Copying Feature**  
   The label copying functionality has been improved to help users better position and copy bounding boxes. This improvement is especially useful when annotating objects of the same class in multiple images.

3. **Optimized Keyboard Shortcuts**  
   Several keyboard shortcuts have been fine-tuned to improve the overall speed and fluency of the annotation process. This change is particularly beneficial for users who need to annotate large volumes of images.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/weixia1/labelme.git
   cd labelme
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Launch the application:
   ```bash
   python __main__.py

## Project Instruction
```bash
Labelme
├── ai # label by deeplearning model
│   ├── __init__.py
│   ├── _utils.py
│   ├── efficient.py
│   ├── segment_anything_model.py
├── cli 
├── config
├── icons # png for software
├── translate # Chinese language
├── utils 
├── widgets
├── __init__.py
├── __main__.py
├── optimizer
├── app.py
├── label_file.pyt
├── logger.py
├── param.py
├── shape.py
├── testing.py
└── requirements.txt
```
