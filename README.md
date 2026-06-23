# Image Captioning AI with Gradio

## Overview

Image Captioning AI is a web-based application that automatically generates descriptive captions for images using the BLIP (Bootstrapping Language-Image Pre-training) model from Salesforce. The application combines Computer Vision and Natural Language Processing (NLP) to understand image content and generate human-readable descriptions.

The project uses Hugging Face Transformers, PyTorch, and Gradio to provide an interactive user interface where users can upload images and receive AI-generated captions instantly.

---

## Features

* Upload images through a web interface
* AI-generated image captions
* Powered by the BLIP Image Captioning model
* User-friendly Gradio interface
* Supports JPG, JPEG, PNG, BMP, and WEBP images
* Fast and accurate image understanding

---

## Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* Gradio
* Pillow (PIL)
* BLIP Image Captioning Model

---

## Project Structure

```text
Image-captioning-ai/
│
├── app.py
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

### Create a Virtual Environment

```bash
python -m venv my_env
```

### Activate the Virtual Environment

Windows:

```bash
my_env\Scripts\activate
```

Linux/macOS:

```bash
source my_env/bin/activate
```

### Install Dependencies

```bash
pip install torch transformers gradio pillow requests
```

---

## Running the Application

Start the Gradio application:

```bash
python app.py
```

You should see output similar to:

```text
Running on local URL: http://127.0.0.1:7860
```

Open the URL in your browser.

---

## How to Use

1. Launch the application.
2. Open the provided local URL in your browser.
3. Upload an image.
4. Click Submit.
5. View the AI-generated caption.

---

## Application Workflow

1. User uploads an image through Gradio.
2. The image is processed by the BLIP processor.
3. The pretrained BLIP model analyzes image content.
4. The model generates a descriptive caption.
5. The caption is displayed in the web interface.

---

## Sample Output

### Input Image

An image containing a dog playing in a grassy field.

### Generated Caption

```text
the image of a dog running through a grassy field
```

---

## Model Information

Model Used:

```text
Salesforce/blip-image-captioning-base
```

The BLIP model is a state-of-the-art vision-language model capable of generating natural language descriptions from images.

---

## Applications

* Accessibility tools for visually impaired users
* Image search and retrieval systems
* Automated image annotation
* Digital asset management
* Social media content generation
* Smart photo organization

---

## Future Improvements

* Multiple caption suggestions
* Real-time webcam captioning
* Support for batch image uploads
* Cloud deployment
* Multilingual caption generation

---

## Author

Abhinav Bhaskar

---

## License

This project is developed for educational and learning purposes. Please refer to the original licenses of Hugging Face, PyTorch, Gradio, and the BLIP model for production usage.
