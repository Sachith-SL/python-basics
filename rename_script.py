import os

image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

image_files = [f for f in os.listdir('.') if f.lower().endswith(image_extensions)]

for index, filename in enumerate(image_files, start=1):
    extension = os.path.splitext(filename)[1]  # Get the file extension
    new_name = f"image_{index}{extension}"
    os.rename(filename, new_name)
    print(f"Renamed: {filename} -> {new_name}")