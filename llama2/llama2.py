from aiohttp import ClientTimeout, ClientSession
import json


class Llama2API:
    def __init__(self, url):
        self.url = url
        self.headers = {'Content-Type': 'application/json'}

    @staticmethod
    def promt_preprocessor(prompt, instructions='', system=''):
        if instructions:
            instructions = f"[INST]{instructions}[/INST]"
        if system:
            system = f"<s><<SYS>>\n{system}\n<</SYS>>\n\n"
        if instructions or system:
            prompt = json.dumps({"prompt": f"{system}{instructions}\nUser: {prompt}"})
        else:
            prompt = json.dumps({"prompt": prompt})
        return prompt

    async def post_prompt(self, prompt, timeout=30):
        session_timeout = ClientTimeout(total=timeout, sock_connect=timeout, sock_read=timeout)
        async with ClientSession(timeout=session_timeout) as session:
            async with session.post(self.url, data=prompt, headers=self.headers) as response:
                response.raise_for_status()
                return await response.json(), response.status

    async def get_prompt(self, prompt):
        async with ClientSession() as session:
            async with session.get(f"{self.url}/{prompt}", headers=self.headers) as response:
                response.raise_for_status()
                return await response.json()
