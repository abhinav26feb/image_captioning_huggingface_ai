import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
print("Loading processor...")
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")


print("Loading model...")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("Model loaded!")

# Hide the main Tkinter window
Tk().withdraw()

# Open file selection dialog
img_path = askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp"),
        ("All Files", "*.*")
    ]
)


# Load your image, DON'T FORGET TO WRITE YOUR IMAGE NAME
# img_path = "./images.jpg"# convert it into an RGB format
image = Image.open(img_path).convert('RGB')

# You do not need a question for image captioning
text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")

# Generate a caption for the image
outputs = model.generate(**inputs, max_length=50)

# Decode the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)
# Print the caption
print(caption)
