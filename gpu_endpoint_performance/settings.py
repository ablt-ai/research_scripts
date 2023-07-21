endpoint_url = "http://100.24.118.194/image_autodescribe"
data = '{"url":"s3://ablt-assets/test/images/cartoon-octopus-free.png"}'
image_sizes = {
    "16:9": [{'width': 2048, 'height': 1152}, {'width': 3840, 'height': 2160}, {'width': 7680, 'height': 4320}, {'width': 1280, 'height': 720}, {'width': 640, 'height': 360}, {'width': 1920, 'height': 1080}, {'width': 480, 'height': 270}, {'width': 320, 'height': 180}, {'width': 32, 'height': 18}],
    "4:3": [{'width': 2048, 'height': 1536}, {'width': 1600, 'height': 1200}, {'width': 1024, 'height': 768}, {'width': 800, 'height': 600}, {'width': 640, 'height': 480}, {'width': 480, 'height': 360}, {'width': 320, 'height': 240}, {'width': 32, 'height': 24}],
    "1:1": [{'width': 2048, 'height': 2048}, {'width': 1600, 'height': 1600}, {'width': 1024, 'height': 1024}, {'width': 800, 'height': 800}, {'width': 640, 'height': 640}, {'width': 480, 'height': 480}, {'width': 320, 'height': 320}, {'width': 32, 'height': 32}]
}
image_sizes_reformatted = [(ratio, size['width'],
                           size['height']) for ratio, sizes in image_sizes.items() for size in sizes]
image_formats = ['bmp', 'gif', 'ico', 'jpeg', 'jpg', 'pdf', 'png', 'psd', 'svg', 'tiff', 'webp']
image_names = ['abstract.png', 'aliens.png', 'art_nouveau.png', 'cyberpunk.png', 'graffiti.png', 'pixel_art.png',
               'pop_art.png', 'robot.png', 'tesla.png', 'valkyries.png', 'vikings.png']