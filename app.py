import gradio as gr
from image_cap_gradio_logic import generate_caption

demo = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Generated Caption"),
    title="Image Captioning AI",
    description="Upload an image and generate a caption."
)

demo.launch(
    server_name="localhost",
    server_port=5000
)