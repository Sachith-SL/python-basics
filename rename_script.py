import os

image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
folder_path = './samples_pngs'

image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]

for index, filename in enumerate(image_files, start=2):
    extension = os.path.splitext(filename)[1]  # Get the file extension
    new_name = f"image_{index}{extension}"

    src = os.path.join(folder_path, filename)   # full source path
    dst = os.path.join(folder_path, new_name)   # full destination path

    os.rename(src, dst)
    print(f"Renamed: {filename} -> {new_name}")