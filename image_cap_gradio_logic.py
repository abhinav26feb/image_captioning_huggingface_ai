from transformers import AutoProcessor, BlipForConditionalGeneration

print("Loading processor...")
processor = AutoProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("Loading model...")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("Model loaded!")

def generate_caption(image):

    inputs = processor(
        images=image,
        text="the image of",
        return_tensors="pt"
    )

    outputs = model.generate(
        **inputs,
        max_length=50
    )

    caption = processor.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return caption