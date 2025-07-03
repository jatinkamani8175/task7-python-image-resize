import os
from PIL import Image

input_dir = 'input_images'
output_dir = 'output_images'
size = (800, 800)

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
        try:
            img = Image.open(os.path.join(input_dir, file))
            img = img.resize(size)
            img.save(os.path.join(output_dir, file.split('.')[0] + '.png'))
        except:
            print(f"Error with file: {file}")
