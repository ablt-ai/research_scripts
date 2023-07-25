from aiohttp import ClientSession, ClientTimeout

import json

from gpu_endpoint_performance.timer import timer


@timer
async def make_post_request(url, data, timeout=300):
    session_timeout = ClientTimeout(total=timeout, sock_connect=timeout, sock_read=timeout)
    async with ClientSession(timeout=session_timeout) as session:
        try:
            async with session.post(url,
                                    headers={"Content-Type": "application/json"},
                                    data=json.dumps({"url": data}),
                                    timeout=timeout) as response:
                response.raise_for_status()
                content = await response.text()
                if "application/json" in response.headers["Content-Type"]:
                    content = await response.json()
                return {"status": response.status, "content": content}
        except Exception as err:
            return {"error": f"Error occurred: {err}"}
