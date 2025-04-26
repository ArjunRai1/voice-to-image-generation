from diffusers import StableDiffusionPipeline
import torch
from recognition import voice_to_text

model = "dreamlike-art/dreamlike-photoreal-2.0"
pipe = StableDiffusionPipeline.from_pretrained(model, torch_dtype=torch.float32, safety_checker=None)
device="cuda"

pipe.to(device)

prompt = voice_to_text()
print(prompt)
image = pipe(prompt,height=512, width=512).images[0]
image.save("generated_image.png")