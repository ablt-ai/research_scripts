import random

import pytest
import asyncio

from gpu_endpoint_performance.request_engine import make_post_request
from settings import endpoint_url, image_sizes, image_formats, image_names, image_storage_url


def exec_async(data):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if len(data) < 2:
        response = asyncio.run(make_post_request(url=endpoint_url, data=data[0]))
        if "error" in response:
            print(f"Request failed, details: {response}")
        else:
            print(response)
    else:
        tasks = []
        for idx in range(len(data)):
            tasks.append(asyncio.ensure_future(make_post_request(url=endpoint_url, data=data[idx])))

        responses = loop.run_until_complete(asyncio.gather(*tasks))
        for response in responses:
            if "error" in response:
                print(f"Request failed, details: {response}")
            else:
                print(response)


@pytest.mark.parametrize("image_aspect", ['4x3', '16x9'])
def test_image_aspects(image_aspect, benchmark, rounds, iterations):
    image_aspect = image_aspect.replace("x", "")
    image_path = f"{image_storage_url}/{image_aspect}/cyberpunk.png"
    benchmark.pedantic(exec_async, [[image_path]], rounds=rounds, iterations=iterations)


@pytest.mark.parametrize("detail", ['1', '2', '3'])
def test_image_complexity(detail, benchmark, rounds, iterations):
    image_path = f"{image_storage_url}/details/details_{detail}.png"
    benchmark.pedantic(exec_async, [[image_path]], rounds=rounds, iterations=iterations)


@pytest.mark.parametrize("image_type", image_formats)
def test_image_types(image_type, benchmark, rounds, iterations):
    image_path = f"{image_storage_url}/formats/robot.{image_type}"
    benchmark.pedantic(exec_async, [[image_path]], rounds=rounds, iterations=iterations)


@pytest.mark.parametrize("aspect_ratio,width,height", [(ratio, size['width'],
                                                        size['height']) for ratio, sizes in image_sizes.items() for size
                                                       in sizes])
def test_image_sizes(aspect_ratio, width, height, benchmark, rounds, iterations):
    image_path = f"{image_storage_url}/sizes/toast_{aspect_ratio.replace(':', 'x')}_{width}x{height}.png"
    benchmark.pedantic(exec_async, [[image_path]], rounds=rounds, iterations=iterations)


@pytest.mark.parametrize("num", [1, 2, 3, 4, 5, 10])
def test_simultaneous_requests(num, benchmark, rounds, iterations):
    image_paths = [f"{image_storage_url}/{random.choice(['43', '169'])}/{random.choice(image_names)}" for _ in range(num)]
    benchmark.pedantic(exec_async, [image_paths], rounds=rounds, iterations=iterations)
