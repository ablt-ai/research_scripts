from gpu_endpoint_performance.request_engine import make_post_request

async def main():
    timeout = 600  # 10 минут

    tasks = [make_post_request(url, data, timeout) for _ in range(10)]  # 10 параллельных запросов
    await asyncio.gather(*tasks)

asyncio.run(main())