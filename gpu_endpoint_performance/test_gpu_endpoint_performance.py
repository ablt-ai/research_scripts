import random

import pytest
import asyncio

from gpu_endpoint_performance.request_engine import make_post_request
from settings import endpoint_url, image_sizes, image_formats, image_names


def exec_async(data):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if len(data) < 2:
        response = asyncio.run(make_post_request(url=endpoint_url, data={"url": data[0]}))
        if "error" in response:
            print(f"Request failed, details: {response}")
        else:
            print(response)
    else:
        tasks = []
        for idx in range(len(data)):
            tasks.append(asyncio.ensure_future(make_post_request(url=endpoint_url, data={"url": data[idx]})))

        responses = loop.run_until_complete(asyncio.gather(*tasks))
        for response in responses:
            if "error" in response:
                print(f"Request failed, details: {response}")
            else:
                print(response)


@pytest.mark.parametrize("image_aspect", ['4x3', '16x9'])
def test_image_aspects(image_aspect, benchmark):
    image_path = f"https://github.com/ablt-ai/research_scripts/blob/main/gpu_endpoint_performance/" \
                 f"test_data/{image_aspect}/cyberpunk.png"
    benchmark.pedantic(exec_async, [[image_path]], rounds=1)

""
@pytest.mark.parametrize("detail", ['1', '2', '3'])
def test_image_complexity(detail, benchmark):
    image_path = f"https://github.com/ablt-ai/research_scripts/blob/main/gpu_endpoint_performance/" \
                 f"test_data/details/details_{detail}.png"
    benchmark(exec_async, [image_path])


@pytest.mark.parametrize("image_type", image_formats)
def test_image_types(image_type, benchmark):
    image_path = f"test_data/formats/robot.{image_type}"
    benchmark(exec_async, [image_path])


@pytest.mark.parametrize("aspect_ratio,width,height", [(ratio, size['width'],
                                                        size['height']) for ratio, sizes in image_sizes.items() for size
                                                       in sizes])
def test_image_sizes(aspect_ratio, width, height, benchmark):
    image_path = f"https://github.com/ablt-ai/research_scripts/blob/main/gpu_endpoint_performance/" \
                 f"test_data/sizes/toast_{aspect_ratio.replace(':', 'x')}_{width}x{height}.png"
    benchmark(exec_async, [image_path])


@pytest.mark.parametrize("num", [1, 2, 3, 4, 5, 10])
def test_simultaneous_requests(num, benchmark):
    image_paths = [f"https://github.com/ablt-ai/research_scripts/blob/main/gpu_endpoint_performance/" \
                   f"test_data/{random.choice(['4x3', '16x9'])}/{random.choice(image_names)}" for _ in range(num)]
    benchmark(exec_async, [image_paths])
