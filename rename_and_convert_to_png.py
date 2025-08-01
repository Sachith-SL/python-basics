import os
from PIL import Image

# Create a list of supported image extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

# Get all image files in current directory
image_files = [f for f in os.listdir('.') if f.lower().endswith(image_extensions)]

# Create output folder (optional)
output_folder = "./converted_pngs"
os.makedirs(output_folder, exist_ok=True)

# Process each image
for index, filename in enumerate(image_files, start=1):
    # Open image using PIL
    try:
        with Image.open(filename) as img:
            # Convert to RGB (if image is not already in that mode)
            img = img.convert("RGBA") if img.mode in ("P", "L", "RGBA", "RGB") else img.convert("RGB")
            
            # Build new filename
            new_name = f"image_{index}.png"
            output_path = os.path.join(output_folder, new_name)
            
            # Save as PNG
            img.save(output_path, "PNG")
            print(f"Converted and renamed: {filename} → {new_name}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
