import os

from PIL import Image

from settings import image_sizes


def resize_image(input_image_path, output_image_path, size):
    print(f"Resizing image {input_image_path}")
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"Original size: {width}x{height}")

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print(f"New size: {width}x{height}")
    resized_image.save(output_image_path)
    print(f"Saved to {output_image_path}")


def resize_image_and_crop(input_image_path, output_image_path, size):
    print(f"Resizing image {input_image_path}")
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"Original size: {width}x{height}")

    # If aspect ratio does not match, if greater - reduce height, else - width
    if width / height > size[0] / size[1]:
        new_height = size[1]
        new_width = int(size[1] * width / height)
    else:
        new_width = size[0]
        new_height = int(size[0] * height / width)

    resized_image = original_image.resize((new_width, new_height))
    print(f"Generated temp image with size: {new_width}x{new_height}")

    # Crop image
    left = (resized_image.width - size[0]) / 2
    top = (resized_image.height - size[1]) / 2
    right = (resized_image.width + size[0]) / 2
    bottom = (resized_image.height + size[1]) / 2

    cropped_image = resized_image.crop((left, top, right, bottom))
    cropped_width, cropped_height = cropped_image.size
    print(f"New size: {cropped_width}x{cropped_height}")
    cropped_image.save(output_image_path)
    print(f"Saved to {output_image_path}")


def resize_all_images(input_image_path, output_image_path):
    base_name = os.path.basename(input_image_path)
    name, ext = os.path.splitext(base_name)

    for ratio, sizes in image_sizes.items():
        for size in sizes:
            new_name = f"{name}_{ratio.replace(':', 'x')}_{size['width']}x{size['height']}{ext}"
            new_image_path = os.path.join(output_image_path, new_name)

            resize_image_and_crop(input_image_path, new_image_path, (size['width'], size['height']))


#resize_all_images("test_data/toast.png", "test_data/sizes/")
#resize_image_and_crop("test_data/toast.png", "test_data/sizes/toast_16.9_7680x4320.png", (7680, 4320))
