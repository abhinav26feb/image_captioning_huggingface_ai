import gradio as gr
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load model and processor once at startup
processor = AutoProcessor.from_pretrained( "Salesforce/blip-image-captioning-base" )
model = BlipForConditionalGeneration.from_pretrained( "Salesforce/blip-image-captioning-base" )
def generate_caption(image):
    inputs = processor(
        images=image,
        text="the image of",
        return_tensors="pt"
    )
    outputs = model.generate(
        **inputs, max_length=50
    )
    caption = processor.decode(
        outputs[0],
        skip_special_tokens=True
    )
    return caption

demo = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Generated Caption"),
    title="Image Captioning AI",
    description="Upload an image and let AI generate a caption." )

demo.launch(server_name="localhost", server_port=5000)