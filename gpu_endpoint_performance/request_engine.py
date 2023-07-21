import requests

from gpu_endpoint_performance.timer import timer


@timer
async def make_post_request(url, data, timeout=1):
    try:
        response = requests.post(url, headers={"Content-Type": "application/json"}, data=data, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"Other error occurred: {err}"}
    else:
        content = response.content
        if "application/json" in response.headers["Content-Type"]:
            content = response.json()
        return {"status": response.status_code, "content": content}
