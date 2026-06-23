# Image Captioning AI Web Application

## Overview

Image Captioning AI is a web-based application that automatically generates meaningful captions for uploaded images using the BLIP (Bootstrapping Language-Image Pre-training) model from Salesforce.

The application combines Computer Vision and Natural Language Processing (NLP) to analyze image content and generate human-readable descriptions through an intuitive Gradio interface.

Users can simply upload an image through their browser and receive an AI-generated caption instantly.

---

## Features

* AI-powered image caption generation
* Web-based user interface using Gradio
* Upload images directly from your computer
* Automatic caption generation using BLIP
* Fast and user-friendly experience
* Powered by Hugging Face Transformers and PyTorch

---

## Technologies Used

* Python
* Gradio
* PyTorch
* Hugging Face Transformers
* Pillow (PIL)
* BLIP Image Captioning Model

---

## Project Structure

```text
Image-captioning-ai/
│
├── app.py                # Gradio web application
├── image_cap.py          # Caption generation logic
├── README.md
├── requirements.txt
└── my_env/
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Image-captioning-ai
```

### Create Virtual Environment

```bash
python -m venv my_env
```

### Activate Virtual Environment

Windows:

```bash
my_env\Scripts\activate
```

Linux/macOS:

```bash
source my_env/bin/activate
```

### Install Required Libraries

```bash
pip install torch transformers gradio pillow requests
```

---

## Running the Application

Start the Gradio application:

```bash
python app.py
```

The application will launch locally and display a URL similar to:

```text
http://localhost:5000
```

Open the URL in your browser.

---

## How to Use

1. Launch the application.
2. Open the localhost URL in your browser.
3. Upload an image from your computer.
4. Click Submit.
5. View the AI-generated caption.

---

## Application Workflow

1. User uploads an image through the Gradio interface.
2. The image is sent to the BLIP processor.
3. The pretrained BLIP model analyzes the image.
4. The model generates a descriptive caption.
5. The caption is displayed in the web application.

---

## Sample Output

### Uploaded Image

A dog running through a grassy field.

### Generated Caption

```text
the image of a dog running through a grassy field
```

---

## Model Information

Model Used:

Salesforce/blip-image-captioning-base

The BLIP model is a vision-language model developed by Salesforce Research that can understand visual content and generate natural language descriptions.

---

## Future Enhancements

* Multiple caption suggestions
* Real-time webcam captioning
* Batch image processing
* Cloud deployment
* Multilingual caption generation
* Caption confidence scores

---

## Applications

* Accessibility tools for visually impaired users
* Automated image annotation
* Digital asset management
* Image search and retrieval
* Social media content generation
* Smart photo organization

---

## Author

Abhinav Bhaskar

---

## License

This project is developed for educational and learning purposes. Please refer to the respective licenses of Gradio, PyTorch, Hugging Face Transformers, and the BLIP model for production use.
