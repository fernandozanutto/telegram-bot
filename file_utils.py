from PIL import Image

def resize_file(file_path: str) -> str:
    image = Image.open(file_path)
    sizes = image.size
    x = sizes[0]
    y = sizes[1]

    if x > y:
        ratio = x / 512
    else:
        ratio = y / 512

    new_x = x/ratio
    new_y = y/ratio

    new_image = image.resize((int(new_x), int(new_y)))

    if not file_path.endswith(".png"):
        file_path = file_path[:-4] + ".png"

    new_image.save(file_path)

    return file_path
