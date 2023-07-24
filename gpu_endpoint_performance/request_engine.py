from aiohttp import ClientSession

from gpu_endpoint_performance.timer import timer


@timer
async def make_post_request(url, data, timeout=600):
    async with ClientSession() as session:
        try:
            async with session.post(url,
                                    headers={"Content-Type": "application/json"}, data=data,
                                    timeout=timeout) as response:
                response.raise_for_status()
                content = await response.text()
                if "application/json" in response.headers["Content-Type"]:
                    content = await response.json()
                return {"status": response.status, "content": content}
        except Exception as err:
            return {"error": f"Error occurred: {err}"}
